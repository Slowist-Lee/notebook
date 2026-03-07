# 文献

## 1. Benchmark 1（Energy Efficient or Exhaustive? ）

- 这篇主要提供了Benchmark

目前主流模型：
Transformers：没有做特殊的inference engine处理
vLLM： designed for highthroughput LLM serving， PagedAttention
Microsoft’s DeepSpeed: Distributed training - ZeRO
TensorRT-LLM: 特制Nvidia GPUs, 融合Triton

这篇文章做什么：quantify the power consumption of LLM inference lifecycle on inference engines and provides the measurement methodology we used for breakdown analysis.

创新：细粒度分析：Decomposing the inference lifecycle into two stages: (1) the setup stage, which includes engine initialization and model loading steps; and (2) the token generation stage, where actual inference takes place.

准备阶段 Setup：$E_{IE}$: 推理引擎（Inference Engine）$E_{LM}$: 加载大语言模型（LLM）的能耗，将LLM从硬盘搬到显存

生成阶段TG (Token Generation) $=T \times E_{PT}$ (Per Token)

![|475](Pasted%20image%2020260304205810.png)

能耗测GPU,CPU,DRAM

![](Pasted%20image%2020260304210202.png)

### 具体怎么测？

使用 **IPMI** 监控整机的总输入功耗；使用 **NVML** (NVIDIA Management Library) 实时收集GPU的功耗；使用 **Intel RAPL** 记录CPU和内存（DRAM）的功耗

（他们已经分别用专门的工具（NVML 和 Intel RAPL）精准测出了 GPU、CPU 和 内存（DRAM）这三大耗电大户的具体功耗，那么 **IPMI 测出的系统总功耗**）

Setup测： latency(TTFT — Time to first token) and energy consumption of initialing engines and loading LLMs until first token.

TG测：we measured three types of energy consumption during inference: energy per token, energy per response and energy per second. 

Energy/throughput ratio: we evaluated the relationship between energy efficiency and throughput of each engine.

测量结果：

### Load

1. TTFT：
- setup(loading engine) Transformers和DeepSpeed表现好，TensorRT-LLM和vLLM要30s
- loading LLM: time: vLLM > ... > Transformers & DeepSpeed
为什么？
vLLM: 要设置 PagedAttention, TensorRT-LLM: model compilation

vLLM’s initialization involves setting up “PagedAttention” for efficient memory management and configuring distributed inference for token generation process; TensorRT-LLM requires extensive model compilation, including layer fusion, and hardware-specific CUDA kernel generation.

加速 token generation的时候，同时让 load engines 和 LLMs 变慢了

![](Pasted%20image%2020260304210251.png)

### Token Generation

**1. 标准负载 (Standard Load)**

- **参数配置**：Batch size 设为 128，生成 500 个 Token。
- **实际意义**：这模拟的是服务器处于**常规、平稳运行状态**下的场景。此时系统需要同时处理中等数量的用户并发请求（128个），并且每个请求只需要模型回复一段中等长度的内容（比如几句简单的日常问答或小段文本摘要）。

**2. 高并发 (High Concurrency)**

- **参数配置**：Batch size 提升到 256，生成 500 个 Token。
- **实际意义**：相比于标准负载，这里的并发请求数直接翻倍。这模拟的是**业务高峰期（如热点事件爆发、特定时间段的流量激增）**。系统面临大量用户在同一时间涌入提问，但每个问题依然是中等长度的回复。这个负载主要用来测试推理引擎在面对“海量并发请求”时的内存管理能力（比如能不能在一瞬间塞下那么多请求而不崩溃）以及算力分配能力。

vLLM最好，因为 lowest energy per token by optimizing GPU utilization for large batch sizes 

**3. 高吞吐量 (High Throughput)**

- **参数配置**：Batch size 保持 256，但生成的 Token 数大幅增加到 2000 个。
- **实际意义**：这是这三个测试中**最极限、压力最大**的场景。它不仅要求系统同时处理海量的并发请求（256个），还要求系统为每一个请求都生成非常长的连贯文本（2000个Token，相当于长篇大论）。这模拟的是**重度内容生成业务**，例如批量生成长篇文章、深度的代码编写、长篇小说创作或复杂的财报分析等。这个负载旨在逼出系统硬件的极限，测试引擎在持续满负荷运转时的极致吞吐性能和能效表现。

vLLM和TensorRT-LLM效果相对好

---


**总结来说：** 作者通过这三个负载形成了阶梯式的压力测试。在这套测试下，轻量级的引擎（如Transformers）在“标准负载”还能应付，但一旦进入“高并发”或“高吞吐量”就会显得极其吃力、极其耗电；而专为大规模服务设计的引擎（如vLLM和TensorRT-LLM）则是在“高吞吐量”的重压下，反而展现出了极高的硬件利用率和极其省电的单Token能耗优势。

vLLM和TensorRT-LLM是对energy-efficient的

### Power Consumption / Response

TensorRT-LLM achieved the lowest total energy at 510.4 J, while its efficient GPU energy of 232.1 J accounts for 45% of total energy per response. vLLM consumed the highest energy at 700.8 J per response.

为什么vLLM能量最高的解释——输出的token数量最多：While vLLM demonstrates the best energy efficiency per token, it shows the worst energy consumption per response. This contrast arises because different engines applies different ending policy of inference, the actual number of output tokens are different. vLLM generates the largest number of tokens per response on Alpaca dataset. So the total energy per response is highest compared to other engines.

### Power Consumption / Second

TensorRT-LLM 最省，vLLM依旧是最大的，DeepSpeed 和 vLLM 类似 

Transformers consumes the least DRAM energy due to its memory utilization technique

### Energy Efficiency/Throughput Ratio

energy/token 和 throughput 这里的围出来的面积是 energy per second 因为：

![|400](Pasted%20image%2020260305173250.png)

![|425](Pasted%20image%2020260305173121.png)


idle 空闲： GPUs and CPUs consume substantial baseline power at about 120W.

当系统处理高并发或高吞吐量的工作时，总功耗会飙升到约 **1000W** ，尽管总耗电量大幅增加，但**生成每个 Token（大模型处理文本的基本单位）的平均能耗反而下降了**。因为那 120W 的固定“开机/怠速成本”被分摊到了单位时间内大量生成的 Token 上。产出越多，分摊到每个单位上的固定成本就越低。

"If researchers can improve the performance and throughput of a inference engine, the energy efficiency will also be improved." 基于上述原理，如果研究人员能够通过技术手段提升推理引擎的性能和吞吐量（让它在单位时间内算出更多的词），那么系统的整体能源效率也会随之提高。

### 选择标准：

For latency-sensitive or on-demand environments 对延迟敏感 , DeepSpeed and transformers

intensive inference： vLLM / TensorRT-LLM

展望：
① large-scale clusters上的测试
② 开发一个集合了优点的llm： propose to design and develop a novel energy-efficient inference engine or framework that integrates the strengths of existing systems
## 2. Benchmark 2: Words to Watts

inference experiments on LLaMA: 主要关注 compute performance and energy 在 multi-node/multi-GPU 上的表现 —— evaluate the inference performance, latency, and inference energy costs of LLaMA 65B

这篇论文用了 LLaMA 65B，同时也用了 7B和13B，在MIT Sumpercloud HPC System，使用了两个dataset

大规模用的V100，小规模 A100

测量方法：

1. Inference performance is measured in terms of rates: words, tokens, and responses per second or, equivalently, the number of words, tokens, and responses generated per second.
2. monitor GPU 主要使用 `nvidia-smi` 和 `NVIDIA DCGM` : study GPU utilization, energy, power draw


---

测量结果：

1. Inference Performance：参数量：7/13/65B的区别：A100优于V100，尤其是小参数（7，13B），across words per second, tokens per second, and responses per second 。 65B上提升没那么显著，是因为需要模型切分，跨节点的通信开销抵消了 A100 单卡的高性能优势。LLaMA 7B 在 Alpaca 上的提升比 GSM8K 更明显，可能是dataset complexity的区分。 

但更高的inference throughput 会带来 increased energy cost per second

2. Energy per Second: 能源代价：所有尺寸 A100都比V100 更 cost energy，7B的能耗增加最明显，对于最大的 **65B 模型**，由于 A100 带来的吞吐量提升非常微小（受限于跨节点通信），作者质疑为了这点提升而付出更高昂的每秒能耗成本是否值得

3. Energy per Decoded Token: **分片越多，功耗越高**：增加分片数量（即使用更多 GPU）会直接导致瓦特（Wattage）数的增加。即使在相同的 Batch Size 下，增加分片也会推高能耗。【这一个Energy per Response 也同理】

- 在 GSM8K 数学数据集、16 分片、生成长度 512 的特定配置下，增加 Batch Size 反而能**降低**单个 Token 的能耗。
    
- 但这个“最优解”非常脆弱，当生成长度变为 1024 时就会消失。

Energy per Response 512->1024不会对inference energy costs 产生明显或显着的影响。 batch size增加 energy cost会增加但不明显。GSM8K在512/16依旧有一个拐点

Power Capping (一种手段)：
LLaMA 65B 4 A100 80GB 设置200，175，150W
power cap 250-175 推理时间没有明显变化，但到150变化就很大  => power capping as an energy savings intervention can be effective when applied appropriately. 

static 不一定好，最好按实验区分

最后：GPU Resource Utilization 64 batch_size 然后 length 256
测量方法：DCGM

1. 实验设置背景

- **任务**：运行 65B 参数量 LLaMA 模型的切片推理（Model Sharded Inference，通常指张量并行 Tensor Parallelism 或流水线并行 Pipeline Parallelism）。
    
- **配置**：Batch Size 为 64，最大生成长度设定为 256 或 2048。
    
- **硬件**：测试了 4 张 A100（80GB）以及 8/16/32 张 V100 GPU。
    

2. 核心发现：计算与显存的“冰火两重天”

- **计算资源（SM）高度饱和**：通过 DCGM 工具监测，GPU 的流式多处理器（Streaming Multiprocessors, SM）利用率非常高，达到了 94%-95%。当生成长度增加到 2048 时，A100 的 SM 利用率甚至飙升到了 98%。这意味着 GPU 的计算核心几乎满负荷运转。
    
- **显存容量（Memory Capacity）严重闲置**：由于模型被切片（Sharded）分布在多张卡上，平摊到每张 80GB 的 A100 上后，显存占用率仅为 23%-27%。即使加上 Batch Size 64 的 KV Cache 和中间激活值，显存空间依然有大量富余。


> [!note]+ GPU资源
> - **计算资源（Compute / SMs / Tensor Cores）—— “加工机器”**
>     
>     - 代表 GPU 做数学运算（如矩阵乘加 MAC）的速度。衡量指标通常是 **TFLOPS**（每秒万亿次浮点运算）。
>         
>     - **职责**：负责把输入的数据变成输出的数据。
>         
> - **显存容量（Memory Capacity）—— “静态仓库”**
>     
>     - 代表 GPU 能装下多少数据，比如 A100 的 80GB。
>         
>     - **职责**：存放模型权重（Weights）、中间激活值（Activations）、KV Cache 等。如果仓库不够大（Out of Memory, OOM），即使机器再快也无法开工。


3. MLSys 优化启示：混部技术 (Co-location)

作者指出，这种 **“算力拉满、显存空虚”** 的状态意味着系统资源没有被最优化利用。为了榨干 GPU 的价值，他们提出了未来的研究方向：

- **多任务混部 (Co-location)**：既然显存还空着一大半，完全可以在同一批 GPU 上同时加载其他的模型或任务。
    
- **硬件/底层技术支持**：为了实现安全的混部并减少任务间的干扰，作者提到了 Nvidia 的两项关键 GPU 共享技术：
    
    - **MPS (Multi-Process Service)**：允许多个进程共享同一个 GPU 的上下文，提升并发执行效率。
        
    - **MIG (Multi-Instance GPU)**：硬件级别的隔离，将一块大 GPU（如 A100）在物理上切分成多个实例，各自拥有独立的显存和计算资源。
        


简单来说，这段话传达的核心信息是：**在分布式 LLM 推理场景下，算力往往是瓶颈（SM利用率极高），而显存容量却有大量剩余。通过 MPS 或 MIG 等技术将多种 Workload 混合部署在同一张卡上，是未来提升集群整体吞吐量（Throughput）和降低云端成本的关键思路。**





展望：
While we do not control for the correctness/quality of the outputs or the complexity of the inputs/outputs in studying trade-offs between inference energy and performance, we hope to account for this as an ablative study in future work.


