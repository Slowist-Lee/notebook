
请根据以下笔记，完善cpp文件这份课程设计。课程设计要求如图。
---
笔记：


> 对应m8b

好的，这是一份根据您提供的课件整理的关于“信道均衡”的 Obsidian Markdown 笔记。笔记内容涵盖了课件中的所有知识点，并按照原始顺序组织。

---

好的，这是一份根据您提供的课件整理的关于 **信号空间 (Signal Space)** 的 Obsidian Markdown 笔记。笔记涵盖了课件中的所有知识点，并使用了相应的格式。

---
好的，这是根据您提供的课件整理的 Obsidian Markdown 笔记。笔记内容涵盖了每一页的知识点，并使用了 Markdown 格式、数学公式以及 Obsidian Callout，便于您学习和回顾。

---

# Lecture 10: 通用M元调制与解调

## 概览与回顾

> [!summary] 核心内容
> 本讲将重点讨论 M 元调制、最佳信号检测，以及如何在加性高斯白噪声（AWGN）信道下，为通用的 M 元信号传输设计能最小化错误概率 $P_e$ 的最佳接收机。

### 已学知识回顾 (Have Considered)
- **信号的几何表示法**:
    - **信号空间与信号向量**: 将信号视为高维空间中的向量。
    - **信号空间维度**: 信号空间由一组线性无关的向量（基函数）张成。
    - **基向量/基函数**: 正交/标准正交信号集。
    - **格拉姆-施密特正交化 (GSO) 过程**: 一种系统性地确定一组标准正交基的方法。

### 本讲主要内容 (We will now consider)
- **M元调制 (M-ary Modulation)**
- **最佳信号检测 (Optimum signal detection)**
- 在 **AWGN** 信道背景下，确定能够最小化错误概率 $P_e$ 的通用M元信号传输的最佳接收机。

---

## 数字通信系统回顾

### 三个基本组成部分
1.  **发送端 (Transmitter)**: 或数字调制器。
2.  **接收端 (Receiver)**: 或数字解调器。
3.  **信道 (Channel)**: 信号传输的媒介。

### 关键指标
- **质量/性能度量 (Quality/Performance Measure)**:
    - 误比特率 (Bit Error Rate, BER)
    - 比特率 (Bit Rate)
- **资源 (Resource)**:
    - 带宽 (Bandwidth)
    - 功率 (Power)

> [!info] 核心权衡
> 数字通信系统设计的核心在于**比特率 (Bit Rate)**、**带宽 (Bandwidth)**、**功率 (Power)** 和 **错误概率 (Error Probability)** 这四个基本参数之间的权衡。
> 

### 信道示例：AWGN
- **AWGN (Additive White Gaussian Noise)**: 加性高斯白噪声。
- 接收信号 $y(t)$ 是发送信号 $x(t)$ 和噪声 $n(t)$ 的和：
    $$
    y(t) = x(t) + n(t)
    $$
- 在这种理想信道模型中，信道仅引入噪声，不产生其他形式的失真。

---

## 数字调制器 (Digital Modulator)

### 基本概念
- **调制符号 (Modulation symbols)**:
    - 具有有限持续时间 $T_s$ 的信号脉冲。
    - 例如，二进制调制器输入1个比特 {0,1}，从集合 $\{s_0(t), s_1(t)\}$ 中输出一个调制符号。
- **波特率 (Baud Rate) / 符号速率 (Symbol Rate)**: 每秒传输的符号数。
    $$
    R_{baud} = \frac{1}{T_s}
    $$
- **比特率 (Bit Rate)**: 单位为 bps (bits per second)。
    $$
    \text{Bit Rate} = (\frac{1}{T_s}) \times (\frac{\text{bits}}{\text{symbol}})
    $$
- **传输带宽 (Transmission BW)**:
    $$
    W = \frac{1}{T_s}(1+\alpha)
    $$
    其中 $\alpha$ 是滚降系数。
- **M元调制器 (M-ary Modulator)**:
    - 从 M 个可能的符号 $\{s_1(t), s_2(t), ..., s_M(t)\}$ 中选择一个进行发送。



### 调制器参数规范
- **符号持续时间 $T_s$**: 调制器产生一个调制符号的频率。
- **信号集 $S_M$**: 调制器使用的 M 个时域信号的集合。
    $$
    S_M = \{s_1(t), ..., s_M(t)\}
    $$
- **发射带宽 $W_{tx}$**:
    $$
    W_{tx} = (1+\alpha)\frac{1}{T_s}
    $$
- **发射功率 $P_{tx}$**:
    $$
    P_{tx} = \frac{1}{MT_s} \sum ||\vec{s}_m||^2 = \frac{1}{MT_s} \sum \int_0^{T_s} |s_m(t)|^2 dt
    $$

### 信号集的表示方法
1.  **时域 (Time Domain)**: 直接用波形函数表示。
2.  **几何域 (Geometric Domain) / 星座图 (Constellation)**:
    - M 个调制信号可以被几何地表示为信号空间中的 M 个点。
    - M 元调制器可以由 D 维信号空间中的 M 个点来表示，这被称为调制器的**星座图**。

#### 能量与功率
- **调制器的平均能量 (Average Energy)**:
    - 等价于星座图中所有点到原点距离平方的平均值。
    $$
    E = \frac{1}{M} \sum_{i=1}^{M} ||\vec{s}_i||^2
    $$
- **平均发射功率 (Average Transmit Power)**:
    $$
    P_{tx} = \frac{1}{T_s} E = \frac{1}{MT_s} \sum_{i=1}^{M} ||\vec{s}_i||^2
    $$

---

## M元调制实例

### QPSK (Quadrature Phase Shift Keying)
- 每个符号携带 **2 bits**。
- 比特率 = 2 × 符号速率。
- 

### 8PSK (8-Phase Shift Keying)
- 每个符号携带 **3 bits**。
- 比特率 = 3 × 符号速率。
- 

### 16-QAM (16-Quadrature Amplitude Modulation)
- 每个符号携带 **4 bits**。
- 比特率 = 4 × 符号速率。
- 

### FSK (Frequency Shift Keying)
- **Binary FSK**: 每个符号携带 1 bit。
- **4FSK**: 信号集有4种不同的频率（tones），每个符号携带 2 bits。
- **MFSK**: 通用的 M 元频移键控。
- 

---

## 接收信号与噪声

### 时域视图 (Time Domain View)
- 经过 AWGN 信道的接收信号为：
    $$
    y(t) = \underbrace{x(t)}_{\text{transmitted signal}} + \underbrace{n(t)}_{\text{random noise}}
    $$
> [!question] 核心问题
> 如何基于观测到的、含有噪声的波形 $y(t)$，做出最佳的检测（判决）？

### 几何域视图 (Geometric Domain View)
- 信号和噪声都可以表示为向量形式：
    $$
    \vec{y} = \vec{x} + \vec{n}
    $$
- 噪声向量 $\vec{n}$ 会使接收到的信号点 $\vec{y}$ 偏离原始的发送信号点 $\vec{x}$（或 $\vec{s}_i$），形成一个以 $\vec{s}_i$ 为中心的“噪声云”。
- 

### 噪声向量的性质
假设 M 个可能发送的信号 $\{\vec{s}_1, \vec{s}_2, ..., \vec{s}_M\}$ 位于一个由标准正交基 $\{\phi_1(t), ..., \phi_N(t)\}$ 张成的 N 维信号空间中。

1.  **信号空间内的投影**:
    - 发送信号 $x(t)$ 完全位于该信号空间内。
    - 信道白噪声 $n(t)$ 可能不完全在该信号空间内。
    - **关键**：$y(t)$ 在信号空间之外的分量与已发送信息无关，对检测过程没有帮助。
    - **最优性**: 我们可以无损地将接收信号 $y(t)$ 投影到 N 维信号空间，以获得所有有用的分量。
        - 发送信号向量: $\vec{x} = (x_1, ..., x_N)$，其中 $x_n = \int_0^{T_s} x(t)\phi_n^*(t)dt$
        - 接收信号向量: $\vec{y} = (y_1, ..., y_N)$，其中 $y_n = \int_0^{T_s} y(t)\phi_n^*(t)dt$

2.  **噪声向量 $\vec{n}$ 的统计特性**:
    - **性质 I**: 噪声向量 $\vec{n}$ 是一个**高斯随机向量**。
      - 这是因为 $n(t)$ 是一个高斯白噪声过程，而 $n_n = \int_0^{T_s} n(t)\phi_n^*(t)dt$ 是高斯过程的线性变换。
    - **性质 II**: 噪声向量的**均值为 0**。
      $$
      E[n_n] = E[\int_0^{T_s} n(t)\phi_n^*(t)dt] = \int_0^{T_s} E[n(t)]\phi_n^*(t)dt = 0
      $$
    - **性质 III**: 噪声向量的分量是**独立同分布 (i.i.d.)** 的，方差为 $\eta_0/2$。
      $$
      E[n_i n_j^*] = \frac{\eta_0}{2} \int_0^{T_s} \phi_i^*(t)\phi_j(t)dt =
      \begin{cases}
      \eta_0/2 & \text{if } i=j \\
      0 & \text{otherwise}
      \end{cases}
      $$

---

## 解调器 (Demodulator) 的任务

### 检测 (Detection)
- 给定接收到的观测点 $\vec{y}$，从 M 个可能的发送点 $\{\vec{s}_1, ..., \vec{s}_M\}$ 中，解码或找出究竟是哪一个信号被发送了。

### 最佳检测 (Optimal Detection)
- 给定观测值 $\vec{y}$，对携带的信息比特做出**最佳猜测 (best guess)**。
- “最佳”的定义是**最小化误比特率 (BER)**。

> [!question] 两个核心问题
> 1.  **Q1) 最佳解调器是什么？**
>     - 在 AWGN 信道下，**最小距离检测 (Minimum Distance Detection)** 是最佳的。
>     - 它的实现结构是怎样的？
> 2.  **Q2) 使用“最小距离检测”的错误性能如何？**
>     - 使用最佳解调器时，我们还会犯错吗？（会）
>     - 犯错的机制是什么？

### 最小距离检测 (Minimum Distance Detection)

#### 最优性
- 可以证明，最佳检测器非常简单：选择与接收向量 $\vec{y}$ **欧氏距离最近**的信号向量。
    $$
    \vec{s}^* = \arg \min_{\vec{x} \in \{\vec{s}_1, ..., \vec{s}_M\}} ||\vec{y} - \vec{x}||^2
    $$
- 

#### 结构 (Architecture)
1.  **步骤1**: 将时域接收信号 $y(t)$ 转换为几何域的接收向量 $\vec{y}$ (通过一组相关器或匹配滤波器实现)。
2.  **步骤2**: 计算 $\vec{y}$ 与 M 个可能的信号点 $\vec{s}_m$ 之间的 M 个距离。
3.  **步骤3**: 确定最小距离，并选择对应的符号作为判决结果。

#### 解调器结构与简化
- 最小化欧氏距离 $||\vec{y} - \vec{s}_m||^2$ 的计算可以展开：
    $$
    d(y(t), s_m(t))^2 = ||\vec{y} - \vec{s}_m||^2 = ||\vec{y}||^2 + ||\vec{s}_m||^2 - 2 \langle \vec{y}, \vec{s}_m \rangle
    $$
- 展开后为：
    $$
    ||\vec{y}||^2 + E_m - 2 \int y(t)s_m^*(t)dt
    $$
- 由于 $||\vec{y}||^2$ 对所有 $m$ 都是常数，因此最小化距离等价于最大化下面的表达式：
    $$
    m^* = \arg \max_m \left\{ \int y(t)s_m^*(t)dt - \frac{E_m}{2} \right\}
    $$
- 这导出了一个简化的**相关器接收机**结构。



---

## 错误分析 (Error Analysis)

### 定性分析
- 错误发生的原因是噪声。噪声功率由 $||\vec{n}||^2$ 决定。
- 当噪声足够大，使得接收点 $\vec{y} = \vec{s}_i + \vec{n}$ 落入了另一个信号 $\vec{s}_j$ 的判决区域时，就会发生判决错误。
- 错误概率 $P_e$ 主要由星座图中信号点之间的**最小距离 $d_{min}$** 决定。
    $$
    P_e \approx Q\left( \sqrt{\frac{d_{min}^2}{2\eta_0}} \right)
    $$
    其中 $d_{min} = \min_{i, j, i \neq j} ||\vec{s}_i - \vec{s}_j||$，$Q(\cdot)$ 是标准高斯分布的尾概率函数。



### 定性模型的应用与洞察

> [!info] 设计洞察
> - 比较不同调制方案的优劣。
> - 解释“性能”与“资源”之间的权衡机制。

#### 示例 1: ASK vs FSK
- ASK (振幅键控) 和 FSK (频率键控) 哪种更好？
- 这取决于我们如何定义“更好”。需要比较它们的星座图，分析在相同功率和比特率下的 $d_{min}$。

#### 示例 2: 2D空间中的四元调制
- 在二维信号空间上，有没有比 QPSK 更好的四元调制方案？
- QPSK 将四个点均匀分布在一个圆上，最大化了点之间的最小距离 $d_{min}$，因此在功率效率上是非常优化的。

#### 示例 3: 16QAM vs 16PSK
- 为什么 16QAM 比 16PSK 更受欢迎？
- 在相同的峰值或平均功率下，16QAM 的星座图布局使得其 $d_{min}$ 大于 16PSK 的 $d_{min}$。这意味着在相同的信噪比下，16QAM 的误码性能更好。
    - 16QAM: $d_2 = \frac{\sqrt{2}A_M}{3} \approx 0.471 A_M$
    - 16PSK: $d_1 \approx A_M(\frac{\pi}{8}) \approx 0.393 A_M$
- 

---

## 核心权衡 (Tradeoffs)

> [!summary] 参数关系总结
> - **带宽 (Bandwidth)** ⬆️  ➡️ **比特率 (Bit Rate)** ⬆️
>   - 带宽与符号速率成正比，提高符号速率直接提高比特率。
> - **功率 (Power)** ⬆️  ➡️ **错误概率 (Error Probability)** ⬇️
>   - 增加功率相当于将星座图上的所有点等比例地拉离原点，增大了 $d_{min}$，从而降低了错误概率。
> - **功率 (Power)** ⬆️  ➡️ (间接) **比特率 (Bit Rate)** ⬆️
>   - 增加功率可以支持更密集的星座图（如从 QPSK 升级到 16QAM），在不增加带宽的情况下提高比特率，同时保持可接受的错误概率。
> - **带宽 (Bandwidth)** ⬆️ ➡️ (间接) **错误概率 (Error Probability)** ⬇️
>   - 以 MFSK 为例，增加 M 会同时增加带宽和比特率。在给定的 $E_b/N_0$ 下，符号能量 $E_s = E_b \log_2(M)$ 会增加。同时信号空间的维度也增加到 M，使得信号点在更高维空间中变得更“稀疏”，$d_{min}$ 增大，从而降低了错误概率。

---

## 不同效率目标的调制方案

### 面向高频谱效率 (High Spectral Efficiency)
- **M-ary PSK 和 M-ary QAM**
- **特点**:
    - 信号空间维度始终为 2。
    - 传输带宽对所有 M 保持不变。
    - 比特率: $\text{log}_2(M) \times (1/T_s)$。增加 M 可以在不消耗更多带宽的情况下提高比特率。
- **代价**:
    - 随着 M 的增加，星座点变得更密集，$d_{min}$ 减小。
    - 为保持相同的错误概率，必须**增加发射功率**。
- **结论**: 这类调制方案以**高信噪比 (SNR)** 为代价，实现了**高频谱效率 (Bit rate / BW)**。

### 面向高功率效率 (High Power Efficiency)
- **M-FSK (正交调制)**
- **特点**:
    - 信号集中的信号相互正交。
    - 需要 M 维信号空间来容纳 M 个信号。
    - 额外的维度来自于额外的带宽 (Tx-BW = M × (1/Ts))。
    - 随着 M 增加，信号空间也变得“更大”。
- **优势**:
    - 在相同的 $E_b/N_0$ 下，增加 M 会使星座点之间的距离**增加**，错误概率随之**下降**。
- **结论**: MFSK 善于节省功率（在低 $E_b/N_0$ 下工作），但代价是**带宽的扩展**。

### 案例分析 (Case Study)

> [!question] Case 1: 卫星通信
> **场景**: 为卫星到地球站的通信选择调制方案。
> **分析**: 卫星通信通常是**功率受限**的（卫星上的太阳能电池板功率有限）。因此，应优先选择**功率效率高**的调制方式，如 BPSK, QPSK 或 MFSK。

> [!question] Case 2: 无线视频链路
> **场景**: 在香港大屿山和科技大学之间建立无线视频链路。
> **分析**: 地面无线通信的频谱资源通常是**带宽受限**的。为了传输高清视频所需的高数据率，应选择**频谱效率高**的调制方式，如 16QAM, 64QAM 等。

---

## 最佳检测的数学证明

### 判决区域 (Decision Region)
- 任何解调方案都可以用观测空间 $\mathbf{y}$ 上的一个**判决区域**划分来表示。
- 对于 M 个可能的发送符号 $\{s_1, ..., s_M\}$，观测空间被划分为 M 个互不相交的区域 $\{R_1, ..., R_M\}$。
- 判决规则为：如果接收向量 $\vec{y} \in R_j$，则判决为发送了 $s_j$。
    $$
    R_j = \{\vec{y} : \text{decide } s_j\}
    $$
- 对于等概率信号的最小距离检测器，判决区域的边界是连接任意两个信号点的线段的**垂直平分线**。

### 从平均错误概率推导
- 平均错误概率 $P_e$ 为：
    $$
    P_e = \sum_{j=1}^{M} p(s_j) \int_{R_j^c} p(\vec{y}|s_j) d\vec{y} = 1 - \sum_{j=1}^{M} \int_{R_j} p(s_j)p(\vec{y}|s_j) d\vec{y}
    $$
- 为了最小化 $P_e$，我们需要最大化求和项 $\sum \int_{R_j} p(s_j)p(\vec{y}|s_j) d\vec{y}$。
- 由于每个接收到的 $\vec{y}$ 必须且只能属于一个判决区域 $R_j$，所以最优策略是：对于每一个 $\vec{y}$，都将它分配给能使被积函数 $p(s_j)p(\vec{y}|s_j)$ 最大的那个区域 $R_j$。

### 最佳判决准则
- **最大后验概率 (MAP) 准则**:
    $$
    s^* = \arg \max_{s \in \{s_1, ..., s_M\}} p(s)p(\vec{y}|s)
    $$
- **最大似然 (ML) 检测**:
    - 如果所有 M 个符号是**等概率**的 ($p(s_j) = 1/M$)，MAP 准则简化为最大化**似然函数 $p(\vec{y}|s)$**。
    $$
    s^* = \arg \max_{s \in \{s_1, ..., s_M\}} p(\vec{y}|s)
    $$

### ML 检测与最小距离检测的等价性
- 在 AWGN 信道中，接收向量 $\vec{y} = \vec{s} + \vec{n}$。
- 由于噪声向量 $\vec{n}$ 的分量是均值为0，方差为 $\sigma_n^2 = \eta_0/2$ 的独立高斯随机变量，似然函数为：
    $$
    p(\vec{y}|\vec{s}) \sim \exp\left( -\frac{1}{2\sigma_n^2} ||\vec{y}-\vec{s}||^2 \right)
    $$
- 最大化 $p(\vec{y}|\vec{s})$ 等价于最小化指数部分的正项，即最小化欧氏距离的平方 $||\vec{y}-\vec{s}||^2$。
    $$
    \arg \max_{\vec{s}} p(\vec{y}|\vec{s}) = \arg \min_{\vec{s}} ||\vec{y}-\vec{s}||^2
    $$
> [!success] 结论
> 这证明了在 AWGN 信道和等概率发送符号的条件下，**最小距离检测**就是**最大似然检测**，因此是**最优的**。

---

## 错误概率分析的证明

### 错误概率上界
- 我们要证明：
    $$
    P_e \le Q\left( \sqrt{\frac{d_{min}^2}{2\eta_0}} \right)
    $$
- 假设发送的是 $s_1$，错误事件 $\Psi_1$ 是指接收到的 $\vec{y}$ 离 $s_1$ 的距离不比离其他某个 $s_n$ 的距离更近。
    $$
    \Psi_1 = \bigcup_{n \neq 1} \{||\vec{y}-s_n||^2 \le ||\vec{y}-s_1||^2\}
    $$
- 利用联合界 (Union Bound):
    $$
    P_e(s_1) = P(\Psi_1 | s_1) \le \sum_{n \neq 1} P(||\vec{y}-s_n||^2 \le ||\vec{y}-s_1||^2 | s_1)
    $$
- 对成对错误事件进行分析 $||\vec{y}-s_j||^2 \le ||\vec{y}-s_1||^2$：
    - 代入 $\vec{y} = \vec{s}_1 + \vec{n}$，化简得到：
        $$
        (\vec{s}_j - \vec{s}_1) \cdot \vec{n} \ge \frac{1}{2} ||\vec{s}_j - \vec{s}_1||^2
        $$
    - 令 $Z_j = (\vec{s}_j - \vec{s}_1) \cdot \vec{n} = \int [s_j(t)-s_1(t)]n(t)dt$。$Z_j$ 是一个零均值的高斯随机变量，其方差为：
        $$
        \sigma_Z^2 = \frac{\eta_0}{2} ||\vec{s}_j - \vec{s}_1||^2
        $$
- 成对错误概率 $P_j$ 为：
    $$
    P_j = P\left(Z_j \ge \frac{1}{2}||\vec{s}_j-\vec{s}_1||^2\right) = Q\left(\frac{\frac{1}{2}||\vec{s}_j-\vec{s}_1||^2}{\sqrt{\frac{\eta_0}{2}||\vec{s}_j-\vec{s}_1||^2}}\right) = Q\left(\sqrt{\frac{||\vec{s}_j-\vec{s}_1||^2}{2\eta_0}}\right)
    $$
- 应用联合界，并用最小距离项来近似：
    $$
    P_e \le \sum_{j \neq 1} P_j \approx Q\left(\sqrt{\frac{d_{min}^2}{2\eta_0}}\right)
    $$
- 证明完毕。
	

---

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <string>
#include <fstream>
#include <numeric> // 用于 std::accumulate

// 使用标准命名空间，简化代码
using namespace std;

// =================================================================================
// 1. 常量定义 (CONSTANTS DEFINITION)
// =================================================================================
// --- 根据课程设计要求设置系统参数 ---
const double PI = 3.14159265358979323846;
const double BIT_RATE = 100.0;             // 码元速率 (Rb): 100 bps
const double CARRIER_FREQ = 20000.0;       // 载波频率 (fc): 20 kHz
const double ALPHA = 0.3;                  // 滚降因子 (Roll-off factor) for Raised-Cosine filter
const double SYMBOL_PERIOD = 1.0 / BIT_RATE; // 符号周期 (Tb)

// --- 仿真精度相关的关键参数 ---
// !!关键修正!!: 采样率必须远高于载波频率才能准确表示载波信号。
// 一个常见的工程实践是采样率至少为载波频率的8-10倍。这里我们选择16倍。
const int SAMPLING_RATE_FACTOR = 16;
const double SAMPLING_RATE = SAMPLING_RATE_FACTOR * CARRIER_FREQ; // 系统采样率 (Fs = 320 kHz)
const double TS = 1.0 / SAMPLING_RATE;     // 采样时间间隔

// 每个符号的采样点数，由以上参数导出
const int SAMPLES_PER_SYMBOL = static_cast<int>(SAMPLING_RATE / BIT_RATE); // 320000 / 100 = 3200

// =================================================================================
// 2. 辅助函数 (HELPER FUNCTIONS)
// =================================================================================

/**
 * @brief 生成升余弦滤波器脉冲响应。
 *        这是实现 "Baseband shaping filter" 的核心。
 * @param pulseLength 脉冲的总长度（点数）。
 * @param alpha 滚降因子。
 * @param symbolPeriod 符号周期 (Tb)。
 * @param samplingRate 系统采样率 (Fs)。
 * @return 返回一个包含升余弦脉冲样本的向量。
 */
vector<double> raisedCosinePulse(int pulseLength, double alpha, double symbolPeriod, double samplingRate) {
    vector<double> pulse(pulseLength);
    double T = symbolPeriod;

    for (int i = 0; i < pulseLength; ++i) {
        // 将时间轴中心移到脉冲的中心点，以生成一个对称的脉冲
        double t = (i - pulseLength / 2.0) / samplingRate;

        // 处理 t = 0 的特殊情况，避免 sin(0)/0
        if (abs(t) < 1e-9) {
            pulse[i] = 1.0;
        } 
        // 处理 t = +/- T / (2*alpha) 的特殊情况，避免分母为零
        else if (abs(abs(t) - T / (2 * alpha)) < 1e-9) {
            pulse[i] = (PI / 4.0) * sin(PI / (2 * alpha)) / (PI / (2 * alpha));
        }
        // 通用公式
        else {
            double term1 = sin(PI * t / T) / (PI * t / T);
            double term2 = cos(PI * alpha * t / T) / (1.0 - pow(2.0 * alpha * t / T, 2.0));
            pulse[i] = term1 * term2;
        }
    }
    return pulse;
}

/**
 * @brief 将文本字符串转换为二进制比特流 (ASCII编码，每字符8位)。
 * @param text 输入的文本。
 * @return 代表文本的二进制比特流 (vector<int>)。
 */
vector<int> textToBinary(const string& text) {
    vector<int> binarySequence;
    for (char c : text) {
        // 对每个字符，从最高有效位(MSB)到最低有效位(LSB)转换
        for (int i = 7; i >= 0; --i) {
            binarySequence.push_back((c >> i) & 1);
        }
    }
    return binarySequence;
}

/**
 * @brief 将二进制比特流转换回文本字符串 (ASCII编码)。
 * @param binarySequence 输入的二进制比特流。
 * @return 解码后的文本。
 */
string binaryToText(const vector<int>& binarySequence) {
    string text = "";
    // 确保处理的比特数是8的倍数
    size_t totalBits = (binarySequence.size() / 8) * 8;
    for (size_t i = 0; i < totalBits; i += 8) {
        char c = 0;
        for (int j = 0; j < 8; ++j) {
            if (i + j < binarySequence.size()) {
                c |= (binarySequence[i + j] << (7 - j));
            }
        }
        text += c;
    }
    return text;
}

/**
 * @brief 将信号数据保存到文件，用于后续在其他软件中绘图。
 * @param signal 信号数据。
 * @param filename 文件名。
 */
void saveSignalToFile(const vector<double>& signal, const string& filename) {
    ofstream file(filename);
    if (file.is_open()) {
        for (size_t i = 0; i < signal.size(); ++i) {
            // 第一列是时间，第二列是信号幅值
            file << i * TS << " " << signal[i] << "\n";
        }
        file.close();
    }
}

// =================================================================================
// 3. 通信系统模块 (COMMUNICATION SYSTEM MODULES)
// =================================================================================

/**
 * @brief (a) 基带成形: 将离散的比特序列通过升余弦成形滤波器，生成连续的基带信号。
 * @param bits 输入的比特序列 {0, 1, ...}。
 * @param pulse 成形滤波器的脉冲响应 (即升余弦脉冲)。
 * @return (a)点信号：成形后的基带信号。
 */
vector<double> basebandShaping(const vector<int>& bits, const vector<double>& pulse) {
    // 1. BPSK映射: 将比特 0 映射为幅度 -1, 比特 1 映射为幅度 +1
    vector<double> symbols;
    for (int bit : bits) {
        symbols.push_back(bit == 0 ? -1.0 : 1.0);
    }

    // 2. 升采样: 在每个符号之间插入 SAMPLES_PER_SYMBOL - 1 个零，以匹配系统采样率
    vector<double> upsampledSymbols(symbols.size() * SAMPLES_PER_SYMBOL, 0.0);
    for (size_t i = 0; i < symbols.size(); ++i) {
        upsampledSymbols[i * SAMPLES_PER_SYMBOL] = symbols[i];
    }
    
    // 3. 卷积: 将升采样后的符号序列与成形脉冲进行卷积，实现脉冲成形
    int outputLength = upsampledSymbols.size() + pulse.size() - 1;
    vector<double> shapedSignal(outputLength, 0.0);
    for (size_t i = 0; i < upsampledSymbols.size(); ++i) {
        if (upsampledSymbols[i] != 0) { // 仅在有符号的位置进行计算以提高效率
            for (size_t j = 0; j < pulse.size(); ++j) {
                shapedSignal[i + j] += upsampledSymbols[i] * pulse[j];
            }
        }
    }

    // 4. 截取稳定部分: 卷积会引入延迟，延迟大小为滤波器长度的一半。截取有效部分信号。
    int delay = pulse.size() / 2;
    vector<double> finalSignal(bits.size() * SAMPLES_PER_SYMBOL);
    for(size_t i=0; i < finalSignal.size(); ++i){
        finalSignal[i] = shapedSignal[i + delay];
    }
    
    return finalSignal;
}

/**
 * @brief (b) BPSK调制: 将基带信号调制到载波上。
 * @param basebandSignal (a)点信号：基带信号。
 * @return (b)点信号：调制后的带通信号。
 */
vector<double> bpskModulate(const vector<double>& basebandSignal) {
    vector<double> modulatedSignal(basebandSignal.size());
    for (size_t i = 0; i < basebandSignal.size(); ++i) {
        double t = i * TS;
        // 基带信号直接与载波相乘
        // 乘以 sqrt(2) 是为了使载波信号 cos(2*pi*f*t) 的平均功率归一化为1
        modulatedSignal[i] = basebandSignal[i] * sqrt(2) * cos(2 * PI * CARRIER_FREQ * t); 
    }
    return modulatedSignal;
}

/**
 * @brief (c) AWGN信道: 向信号中添加高斯白噪声。
 * @param signal (b)点信号：原始已调信号。
 * @param snrDb 信噪比 (dB)。
 * @return (c)点信号：添加噪声后的信号。
 */
vector<double> addAWGN(const vector<double>& signal, double snrDb) {
    // 1. 计算信号平均功率
    double signalPower = 0.0;
    for (double s : signal) {
        signalPower += s * s;
    }
    signalPower /= signal.size();

    // 2. 从信噪比(dB)计算噪声功率
    double snrLinear = pow(10.0, snrDb / 10.0);
    double noisePower = signalPower / snrLinear;
    double noiseStdDev = sqrt(noisePower); // 噪声标准差

    // 3. 初始化高斯分布随机数生成器
    random_device rd;
    mt19937 gen(rd());
    normal_distribution<double> dist(0.0, noiseStdDev); // 均值为0，标准差为noiseStdDev

    // 4. 将噪声添加到原信号
    vector<double> noisySignal = signal;
    for (size_t i = 0; i < noisySignal.size(); ++i) {
        noisySignal[i] += dist(gen);
    }
    return noisySignal;
}

/**
 * @brief BPSK相干解调与积分: 乘以同频同相载波，并通过积分器（Integrate and Dump）。
 * @param noisySignal (c)点信号：接收到的带噪声信号。
 * @return (d)点信号：每个符号周期结束时的积分值（采样值）。
 */
vector<double> coherentDemodulateAndIntegrate(const vector<double>& noisySignal) {
    // 1. 相干解调: 将接收信号乘以同频同相的本地载波
    vector<double> multipliedSignal(noisySignal.size());
    for (size_t i = 0; i < noisySignal.size(); ++i) {
        double t = i * TS;
        multipliedSignal[i] = noisySignal[i] * sqrt(2) * cos(2 * PI * CARRIER_FREQ * t);
    }
    
    // 2. 积分器 (Integrate and Dump): 对每个符号周期内的信号进行积分
    int numSymbols = noisySignal.size() / SAMPLES_PER_SYMBOL;
    vector<double> integratedValues; // 这就是 (d) 点的信号
    for (int i = 0; i < numSymbols; ++i) {
        double integral = 0.0;
        // 在一个符号周期内累加所有采样点的值，作为积分的近似
        for (int j = 0; j < SAMPLES_PER_SYMBOL; ++j) {
            integral += multipliedSignal[i * SAMPLES_PER_SYMBOL + j];
        }
        // 积分结果与采样点累加值成正比，这里直接使用累加值进行后续判决
        integratedValues.push_back(integral);
    }
    return integratedValues;
}

/**
 * @brief (e) 判决器: 根据门限判决积分后的值，恢复出比特流。
 * @param integratedValues (d)点信号：积分后的采样值向量。
 * @return (e)点信号：判决出的二进制比特流。
 */
vector<int> decisionDevice(const vector<double>& integratedValues) {
    vector<int> bits;
    // BPSK的最佳判决门限为0
    // 积分值大于0判为'1'，否则判为'0'
    for (double val : integratedValues) {
        bits.push_back(val >= 0 ? 1 : 0);
    }
    return bits;
}


// =================================================================================
// 4. 主函数 (MAIN FUNCTION)
// =================================================================================
int main() {
    // --- 准备工作：生成升余弦脉冲 (一次性生成，供后续重复使用) ---
    // 脉冲长度通常取多个符号周期（如6-8个），以获得较好的带外抑制和时域截断效果
    int pulseDurationInSymbols = 8;
    int pulseLength = pulseDurationInSymbols * SAMPLES_PER_SYMBOL;
    vector<double> rcPulse = raisedCosinePulse(pulseLength, ALPHA, SYMBOL_PERIOD, SAMPLING_RATE);
    
    cout << "=====================================================" << endl;
    cout << "      BPSK Communication System Simulation           " << endl;
    cout << "=====================================================" << endl;

    // --- 任务1: 传输固定序列并保存各点信号用于绘图 ---
    cout << "\n--- Task 1: Fixed Sequence Transmission ---\n" << endl;
    // 根据课程设计要求(1)设置输入序列
    vector<int> testSequence = {0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1};
    cout << "Original bits: ";
    for (int bit : testSequence) cout << bit;
    cout << endl;

    // --- 发送端流程 ---
    // (a) 基带成形
    vector<double> basebandSignal_a = basebandShaping(testSequence, rcPulse);
    // (b) BPSK调制
    vector<double> modulatedSignal_b = bpskModulate(basebandSignal_a);

    vector<double> snrList1 = {-5.0, 5.0};
    for (double snr : snrList1) {
        cout << "\nSimulating for SNR = " << snr << " dB..." << endl;

        // --- 信道与接收端流程 ---
        // (c) 加高斯白噪声
        vector<double> noisySignal_c = addAWGN(modulatedSignal_b, snr);
        // (d) 解调与积分
        vector<double> integratedSignal_d = coherentDemodulateAndIntegrate(noisySignal_c);
        // (e) 判决
        vector<int> decodedBits_e = decisionDevice(integratedSignal_d);
        
        cout << "Decoded bits:  ";
        for (int bit : decodedBits_e) cout << bit;
        cout << endl;
        
        // --- 保存各点信号到文件，用于绘图 ---
        string prefix = "snr_" + to_string((int)snr) + "dB_";
        saveSignalToFile(basebandSignal_a, prefix + "signal_a_baseband.txt");
        saveSignalToFile(modulatedSignal_b, prefix + "signal_b_modulated.txt");
        saveSignalToFile(noisySignal_c, prefix + "signal_c_noisy.txt");

        // (d)点是每个符号末尾的采样值，不是连续信号。将其画在每个符号末尾的时刻点上。
        ofstream d_file(prefix + "signal_d_integrated_samples.txt");
        for (size_t i = 0; i < integratedSignal_d.size(); ++i) {
            d_file << (i + 1) * SYMBOL_PERIOD << " " << integratedSignal_d[i] << "\n";
        }
        d_file.close();

        cout << "Data files for plotting have been saved with prefix: " << prefix << endl;
    }

    // --- 任务2: 传输文本并给出解调结果（计算误码率） ---
    cout << "\n\n--- Task 2: Text Transmission and BER Calculation ---\n" << endl;
    string testText = "The book is suitable for electronic specialties of engineering school in Chinese general institutions of higher learning as the textbook or reference for the junior and senior students and graduate students, and can also be used as a reference book or a textbook in the advanced study classes for the engineering and technical personnel engaged in communication engineering.";
    cout << "Original text length: " << testText.length() << " characters." << endl;
    
    vector<int> textBinary = textToBinary(testText);
    cout << "Total bits to transmit: " << textBinary.size() << endl;

    // --- 发送端 (一次性完成) ---
    vector<double> textBaseband = basebandShaping(textBinary, rcPulse);
    vector<double> textModulated = bpskModulate(textBaseband);

    vector<double> snrList2 = {-10.0, -5.0, 0.0, 5.0, 10.0};
    cout << "\n--- Demodulated Results (BER) for Different SNRs ---" << endl;
    for (double snr : snrList2) {
        // --- 信道与接收端 ---
        vector<double> textNoisy = addAWGN(textModulated, snr);
        vector<double> textIntegrated = coherentDemodulateAndIntegrate(textNoisy);
        vector<int> textDecodedBits = decisionDevice(textIntegrated);
        
        string decodedText = binaryToText(textDecodedBits);
        
        // --- 计算误比特率 (Bit Error Rate, BER) ---
        long long errorCount = 0;
        // 确保比较的长度不超过原始比特流的长度
        size_t bitsToCompare = min(textBinary.size(), textDecodedBits.size());
        for (size_t i = 0; i < bitsToCompare; ++i) {
            if (textBinary[i] != textDecodedBits[i]) {
                errorCount++;
            }
        }
        double ber = static_cast<double>(errorCount) / textBinary.size();
        cout << "SNR = " << snr << " dB -> ";
        cout << "BER: " << ber << " (" << errorCount << "/" << textBinary.size() << " errors)" << endl;
    }
    
    return 0;
}
```


