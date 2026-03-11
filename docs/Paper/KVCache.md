理解KV Cache（键值缓存）的本质，最直接的方法确实是拆解Transformer中注意力机制的数学过程。这不仅能看清“为什么能用”，也能清晰地界定“在什么场景下适用”。

### 一、 从公式推导看：为什么可以用 KV Cache？

标准的缩放点积注意力（Scaled Dot-Product Attention）公式如下：

$$Attention(Q, K, V) = softmax(\frac{QK^T}{\sqrt{d_k}})V$$

在**自回归（Auto-regressive）** 生成模型（如GPT系列）中，文本是一个词一个词生成的。假设我们已经生成了前 $t-1$ 个Token，现在要预测第 $t$ 个Token。

**1. 无 KV Cache 的重复计算灾难**

如果不使用缓存，在第 $t$ 步时，输入序列是 $[x_1, x_2, \dots, x_t]$。我们需要将这 $t$ 个Token全部重新映射，计算出完整的矩阵 $Q_{1:t}$、$K_{1:t}$ 和 $V_{1:t}$，然后再做矩阵乘法。

随着 $t$ 越来越大，每次为了预测一个新Token，都要把前面所有的历史Token重新算一遍，这会产生巨大的算力浪费。

**2. 引入 KV Cache 的数学逻辑**

在因果掩码（Causal Masking）的机制下，第 $i$ 个Token的输出只依赖于它本身和它之前的Token，与未来的Token无关。

因此，在第 $t$ 步时，对于查询（Query），我们真正需要进行注意力计算的，仅仅是当前最新Token $x_t$ 对应的查询向量 $q_t \in \mathbb{R}^{1 \times d}$。

为了计算 $q_t$ 的注意力输出，我们需要它和历史上所有的键（Keys）进行内积运算，得到注意力权重，然后再对所有的值（Values）进行加权求和。

此时，历史的矩阵可以表示为：

$$K_{1:t} = \begin{bmatrix} K_{1:t-1} \\ k_t \end{bmatrix}, \quad V_{1:t} = \begin{bmatrix} V_{1:t-1} \\ v_t \end{bmatrix}$$

注意力分数的计算过程可以拆解为：

$$score_t = q_t K_{1:t}^T = q_t [k_1^T, k_2^T, \dots, k_{t-1}^T, k_t^T]$$

然后进行softmax归一化得到权重向量 $w_t \in \mathbb{R}^{1 \times t}$，最终的输出为：

$$Output_t = w_t V_{1:t} = w_{t,1}v_1 + w_{t,2}v_2 + \dots + w_{t,t-1}v_{t-1} + w_{t,t}v_t$$

**结论：** 从公式中可以看出，为了计算第 $t$ 步的输出，我们只需要当前的 $q_t$、$k_t$、$v_t$，以及过去的 $K_{1:t-1}$ 和 $V_{1:t-1}$。因为历史Token的映射结果 $K$ 和 $V$ 在后续生成中是**完全恒定不变的**，我们直接把前 $t-1$ 步算好的 $K_{1:t-1}$ 和 $V_{1:t-1}$ 存在内存（Cache）里。第 $t$ 步只需要计算出单步的 $k_t$ 和 $v_t$ 拼接进去即可。这就是 KV Cache 成立的数学根基。

---

### 二、 什么情况可以用 KV Cache？

KV Cache 并非在所有阶段和所有模型中都适用。它的使用需要满足特定的结构和场景前提：

**1. 必须是自回归生成阶段（Inference/Decoding）**

- **适用：** 大模型的推理（Inference）阶段。更具体地说，是推理过程中的**解码（Decoding）阶段**。生成第一个Token的过程（Prefill阶段）需要并行处理整个输入Prompt，此时没有历史缓存可用，必须走完整的矩阵乘法。
    
- **不适用：** 模型的训练（Training）阶段。训练时通常采用“Teacher Forcing”策略，整个序列已知，直接通过高度优化的稠密矩阵乘法并行计算所有的 $Q$、$K$、$V$ 效率最高，不需要也不应该逐词使用缓存。
    

**2. 必须是因果注意力（Causal Attention）**

- **适用：** 单向语言模型（如 GPT、Llama 等 Decoder-only 架构）。因为因果掩码保证了历史Token的表示不会受到未来Token的影响，所以历史的 $K$ 和 $V$ 是“固定资产”，可以安全缓存。
    
- **不适用：** 双向语言模型（如 BERT 等 Encoder-only 架构）。在双向注意力中，输入序列长度的改变会改变所有Token的上下文。即使只增加一个新词，前面所有词的 $K$ 和 $V$ 都会因为吸收了新词的信息而发生改变，因此历史表示无法复用。
    

**3. 位置编码机制需支持**

- **适用：** 绝对位置编码（Absolute Positional Encoding）或旋转位置编码（RoPE）、ALiBi 等相对位置编码。这些机制允许在增量推理时，正确地将位置信息注入到新的 $q_t$、$k_t$ 和 $v_t$ 中，而不会破坏已经存入 Cache 的历史张量的有效性。
    

---

通过公式和场景的界定，我们可以看出 KV Cache 是典型的“用空间换时间”的工程优化。你是否需要了解目前业界在 KV Cache 占用显存过大时，常用的优化方案（例如 PagedAttention 或 GQA）？
