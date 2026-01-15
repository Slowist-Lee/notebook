# Lecture 8b: 信道均衡 (Channel Equalization)

## 零码间串扰 (Zero ISI) 的信号设计

### 带限信道的信号设计

为了在带限信道中实现无码间串扰（ISI）的传输，我们需要对发送脉冲 $v(t)$ 进行设计。

- **奈奎斯特零 ISI 条件 (时域)**
  脉冲形状 $v(t)$ 在抽样时刻 $nT$ 的值应满足：
  $$
  v(nT) = 
  \begin{cases}
  1 & n = 0 \\
  0 & n \neq 0
  \end{cases}
  $$
  这个条件意味着在每个符号的抽样时刻，其他符号的“回波”都为零。

- **奈奎斯特零 ISI 条件 (频域)**
  $v(t)$ 的傅里叶变换 $V(f)$ 应满足：
  $$
  \sum_{k=-\infty}^{\infty} V(f + \frac{k}{T}) = T
  $$

- 满足以上条件后，接收机的输出可以简化为：
  $$
  y(t_m) = A_m + n_0(t_m)
  $$
  其中 $A_m$ 是期望的信号幅度，$n_0(t_m)$ 是噪声。

### 奈奎斯特条件：理想情况

奈奎斯特提出的第一种消除 ISI 的方法是使用理想低通滤波器（“砖墙”滤波器）。

- **频域表达式**:
  $$
  V(f) = 
  \begin{cases}
  1 & |f| < \frac{1}{2T} \\
  0 & \text{其他}
  \end{cases}
  $$

- **时域表达式**:
  $$
  v(t) = \frac{\sin(\pi t/T)}{\pi t/T} = \text{sinc}(\frac{t}{T})
  $$



> [!define] 奈奎斯特带宽 (Nyquist Bandwidth)
> $$
> B_0 = \frac{1}{2T} = \frac{R_s}{2}
> $$
> 这是实现零 ISI 所需的最小传输带宽。一个带宽为 $B_0$ 的信道，最高可以支持 $2B_0$ 符号/秒的无码间串扰传输速率。

### 实现奈奎斯特条件的挑战

设计理想的 $v(t)$ 或 $V(f)$ 面临以下挑战：
- **物理不可实现**: $V(f)$ 在通带和阻带之间的过渡是瞬时完成的（陡峭的边沿），这在物理上无法实现。
- **对定时误差敏感**: $v(t)$ (sinc函数) 的衰减速度很慢（按 $1/t$ 衰减），导致接收端对抽样时刻的精度要求非常高，容错边际很小。
- **定时抖动 (Timing Jitter)**: 符号定时不精确是调制解调器/数据接收机设计中的一个主要挑战，这种不精确性被称为定时抖动。

### 实用解决方案：升余弦谱

为了解决理想滤波器的实际问题，我们采用升余弦谱。
- 升余弦谱 $V(f)$ 由三部分组成：**通带 (passband)**、**阻带 (stopband)** 和 **过渡带 (transition band)**。
- 过渡带的形状像一个余弦波，使得频域响应是平滑的，物理上可以实现。

$$
V(f) = 
\begin{cases}
1 & 0 \le |f| < f_1 \\
\frac{1}{2} \left[ 1 + \cos\left( \frac{\pi(|f|-f_1)}{2B_0-2f_1} \right) \right] & f_1 \le |f| < 2B_0-f_1 \\
0 & |f| \ge 2B_0 - f_1
\end{cases}
$$



### 时域脉冲形状

对升余弦谱进行傅里叶反变换，得到时域脉冲 $v(t)$：
$$
v(t) = \text{sinc}(2B_0t) \frac{\cos(2\pi\alpha B_0 t)}{1 - 16\alpha^2 B_0^2 t^2}
$$
其中 $\alpha$ 是滚降系数。

- **$\text{sinc}(2B_0t)$** 项确保了在期望的采样时刻过零。
- **分数项** 使得脉冲旁瓣以 $1/t^2$ 的速度衰减，远快于sinc函数，从而使系统对采样时间误差不那么敏感。



---

## 考虑信道响应的发送/接收滤波器设计

### 最优发送/接收滤波器

> [!summary] 优化目标
> 当使用升余弦谱的 $v(t)$ 满足零ISI条件时，接收滤波器的采样输出为 $Y_m = A_m + N_m$ (假设 $v(0)=1$)。
> 对于二进制PAM传输，$A_m = \pm d$。噪声方差为 $\sigma^2 = \int_{-\infty}^{\infty} S_n(f)|H_R(f)|^2 df$。
> 系统总响应 $V(f) = H_T(f)H_c(f)H_R(f)$。
> 误码率 $P_e = Q(\frac{d}{\sigma})$。
> **目标**：在信道 $H_c(f)$ 和总响应 $V(f)$ 给定的情况下，通过合理选择发送滤波器 $H_T(f)$ 和接收滤波器 $H_R(f)$ 来最大化 $d/\sigma$，从而最小化误码率。

### 最优解

最优策略是在发送端和接收端平均地补偿信道失真。

- **滤波器幅频响应**:
  $$
  |H_T(f)| = \frac{\sqrt{V(f)}}{|H_c(f)|^{1/2}}, \quad |f| \le W
  $$
  $$
  |H_R(f)| = \frac{\sqrt{V(f)}}{|H_c(f)|^{1/2}}, \quad |f| \le W
  $$

- **发送信号能量**:
  根据帕塞瓦尔定理 (Parseval's theorem)，平均发送能量 $E_{av}$ 为：
  $$
  E_{av} = \int_{-\infty}^{\infty} d^2 h_T^2(t) dt = \int_{-\infty}^{\infty} d^2 H_T^2(f) df = \int_{-W}^{W} \frac{d^2 V(f)}{|H_c(f)|} df
  $$
  因此，
  $$
  d^2 = E_{av} \left[ \int_{-W}^{W} \frac{V(f)}{|H_c(f)|} df \right]^{-1}
  $$

- **噪声方差和误码率**:
  接收滤波器输出端的噪声方差为：
  $$
  \sigma^2 = \frac{N_0}{2} \int_{-\infty}^{\infty} |H_R(f)|^2 df = \frac{N_0}{2} \int_{-W}^{W} \frac{V(f)}{|H_c(f)|} df
  $$
  最小误码率为：
  $$
  P_{e,min} = Q\left[ \sqrt{ \frac{2E_{av}}{N_0} \left\{ \underbrace{\int_{-W}^{W} \frac{V(f)}{|H_c(f)|} df}_{\text{由信道失真引起的性能损失}} \right\}^{-1} } \right]
  $$
  
- **特殊情况**: 当 $H_c(f) = 1$ (理想平坦衰落信道)，没有性能损失，结果与AWGN信道下的匹配滤波器接收机相同。

### 练习

- **问题**:
  1.  一个二进制通信系统数据速率 $R=1/T=4800$ bps，信道频率响应为 $|H_c(f)| = \frac{1}{\sqrt{1+(f/W)^2}}$，$|f| \le W$ 且 $W=4800$ Hz。确定最优的发送和接收滤波器。
  2.  加性噪声是零均值高斯白噪声，功率谱密度 $N_0/2 = 10^{-15}$ Watt/Hz。
  3.  要达到 $P_e=10^{-5}$，需要多大的发送能量？

- **解**:
  - 由于 $W=1/T=4800$，我们可以使用滚降系数 $\alpha=1$ 的升余弦谱信号脉冲。
  - 此时的脉冲谱为（根据课件公式）：
    $$
    P(f) = \frac{1}{2}[1 + \cos(\pi|f|/4800)] = \cos^2(\frac{\pi|f|}{9600})
    $$
  - 因此，最优滤波器为：
    $$
    |H_T(f)| = |H_R(f)| = \cos(\frac{\pi|f|}{9600})[1 + (\frac{f}{4800})^2]^{1/4}, \quad \text{for } |f| \le 4800
    $$
  - 利用这些滤波器，可以进一步计算达到特定误码率所需的发送能量。

---

## 存在 ISI 时的性能

- 如果不满足零ISI条件，则接收信号为：
  $$
  Y_m = A_m + \underbrace{\sum_{k \neq m} A_k v[(m-k)T]}_{\text{ISI 项 } A_I} + N_m
  $$
- 通常只考虑 $2M$ 个主要的干扰项：
  $$
  Y_m = A_m + A_I' + N_m, \quad \text{其中 } A_I' = \sum_{k=-M, k \neq m}^{M} A_k v[(m-k)T]
  $$
- 在这种情况下，计算误码率非常困难。通常使用各种近似方法（如高斯近似、切尔诺夫界等）。
- **解决方案是什么？** -> **均衡 (Equalization)**

### 蒙特卡洛仿真 (Monte Carlo Simulation)

这是一种通过仿真来估计误码率的方法。

- **思想**:
  通过大量独立的随机试验，统计错误发生的频率来估计错误概率。
  $$
  \hat{P}_e = \frac{1}{L} \sum_{l=1}^{L} I(X^{(l)})
  $$
  其中 $I(x)$ 是指示函数（发生错误时为1，否则为0），$L$ 是仿真次数。

- **问题**:
  1.  如果希望 $P_e$ 的估计精度在10%以内，需要多少次独立的仿真？
  2.  如果 $P_e \approx 10^{-9}$ (光通信系统典型值)，且每次仿真耗时1毫秒，仿真将需要多长时间？

---

## 均衡 (Equalization)

### 什么是均衡器？

- 我们已经知道，通过合理设计收发滤波器可以保证采样点上无ISI，从而最小化 $P_e$。
- 但这种方法的前提是**信道特性精确已知且不随时间变化**。
- 在实际应用中，信道通常是**未知或时变的**。

> [!define] 信道均衡器 (Channel Equalizer)
> 一种**具有可调节频率响应的接收滤波器**，用于最小化或消除码间串扰 (ISI)。

### 均衡器配置

![均衡器系统框图](https://raw.githubusercontent.com/Klender-J/Image-hosting/main/img/20240105001416.png)

- **总频率响应**:
  $$
  H_O(f) = H_T(f)H_c(f)H_E(f)
  $$
- **零ISI的奈奎斯特准则**:
  $$
  \sum_{k=-\infty}^{\infty} H_O(f + \frac{k}{T}) = \text{常数}
  $$
- **理想的零ISI均衡器**是一个**反转信道滤波器**:
  $$
  H_E(f) \propto \frac{1}{H_T(f)H_c(f)}, \quad |f| \le 1/(2T)
  $$

### 线性横向滤波器 (Linear Transversal Filter)

这是一种常见的均衡器结构，属于**有限冲激响应 (FIR)** 滤波器。

![线性横向滤波器结构](https://raw.githubusercontent.com/Klender-J/Image-hosting/main/img/20240105001423.png)

- **冲激响应**:
  $$
  h_E(t) = \sum_{n=-N}^{N} c_n \delta(t-nT)
  $$
- $\{c_n\}$ 是可调节的均衡器系数（共 $2N+1$ 个）。
- $N$ 的取值需要足够大，以覆盖ISI的持续时间。

---

## 均衡器类型

### 迫零 (Zero-Forcing, ZF) 均衡器

ZF均衡器的目标是“强迫”均衡后脉冲响应在其他符号的抽样时刻上为零。

- **系统模型**:


  - 均衡后的脉冲响应为 $v_{eq}(t) = v_c(t) * h_E(t) = \sum_{n=-N}^{N} c_n v_c(t-nT)$
  - 其中 $v_c(t)$ 是发送滤波器、信道、接收滤波器级联后的等效信道冲激响应。
- **迫零条件**:
  $$
  v_{eq}(mT) = \sum_{n=-N}^{N} c_n v_c[(m-n)T] = 
  \begin{cases}
  1, & m = 0 \\
  0, & m = \pm1, \dots, \pm N
  \end{cases}
  $$
  该条件强迫 $2N$ 个相邻的干扰项为零。

- **矩阵形式求解**:
  将上述方程组写成矩阵形式：
  $$
  \mathbf{v}_{eq} = \mathbf{V}_c \cdot \mathbf{c}
  $$
  其中 $\mathbf{c}$ 是系数向量，$\mathbf{v}_{eq}$ 是 $[..., 0, 1, 0, ...]^T$，$\mathbf{V}_c$ 是信道响应矩阵。
  
  ![ZF均衡器矩阵表示](https://raw.githubusercontent.com/Klender-J/Image-hosting/main/img/20240105001431.png)

- **系数解**:
  $$
  \mathbf{c} = \mathbf{V}_c^{-1} \mathbf{v}_{eq}
  $$
  这等价于取 $\mathbf{V}_c^{-1}$ 的中间一列作为系数向量 $\mathbf{c}$。

#### ZF 均衡器示例
- **问题**: 找到一个五抽头 (five-tap, $N=2$) FIR均衡器的系数，使得主脉冲响应两侧的两个采样点为零。
  ![示例中的脉冲响应vc(t)](https://raw.githubusercontent.com/Klender-J/Image-hosting/main/img/20240105001436.png)
- **解**:
  1.  通过观察上图得到 $v_c(nT)$ 的采样值。
  2.  构建 $5 \times 5$ 的信道响应矩阵 $\mathbf{V}_c$。
  3.  计算 $\mathbf{V}_c$ 的逆矩阵 $\mathbf{V}_c^{-1}$ (例如使用MATLAB)。
  4.  $\mathbf{V}_c^{-1}$ 的中间一列就是所求的系数 $\{c_{-2}, c_{-1}, c_0, c_1, c_2\}$。
  5.  可以验证，使用这些系数后，$v_{eq}(0)=1.0$ 且 $v_{eq}(m)=0, m=\pm1, \pm2$。
- **注意**: ZF均衡器只保证了在有限个点（$m=\pm1, \dots, \pm N$）上的ISI为零。在这些点之外，仍然可能存在**残留ISI**。

### 最小均方误差 (MMSE) 均衡器

> [!warning] ZF均衡器的缺点
> - 忽略了加性噪声的影响。
> - 在试图反转信道时，如果信道在某些频率有深度衰落，ZF均衡器会极大地放大噪声。

MMSE均衡器提供了一种替代方案。
- **基本思想**:
  - 放松严格的迫零条件。
  - 在均衡器输出端，最小化**残留ISI**和**加性噪声**的总功率。

> [!define] MMSE均衡器
> 一种基于最小均方误差 (Minimum Mean-Square Error, MMSE) 准则进行优化的信道均衡器。

#### MMSE 准则

![MMSE均衡器系统模型](https://raw.githubusercontent.com/Klender-J/Image-hosting/main/img/20240105001441.png)

- **目标**: 最小化均方误差 (MSE)
  $$
  \text{MSE} \triangleq E\left[ (z(mT) - A_m)^2 \right] = \text{Minimum}
  $$
  其中 $z(mT)$ 是均衡器输出，$A_m$ 是期望的输出（即原始发送符号）。

- **MMSE解 (Wiener-Hopf方程)**:
  通过令 $\frac{\partial \text{MSE}}{\partial c_n} = 0$ 得到最优系数，最终导出以下方程组：
  $$
  \sum_{n=-N}^{N} c_n R_y(n-k) = R_{AY}(k), \quad \text{for } k=0, \pm1, \dots, \pm N
  $$
  - $R_y$ 是均衡器输入信号 $y(t)$ 的自相关函数。
  - $R_{AY}$ 是期望输出 $A_m$ 和输入信号 $y(t)$ 的互相关函数。
  - 期望 $E[\cdot]$ 是对所有数据符号 $A_m$ 和加性噪声取的。

- **实际应用**:
  $R_y$ 和 $R_{AY}$ 可以通过在发送端发送一个已知的训练序列（test signal），然后在接收端进行时间平均来估计。

### MMSE 均衡器 vs. ZF 均衡器

- 两者都可以通过求解类似形式的线性方程组得到。
- ZF 均衡器不考虑噪声的影响。
- MMSE 均衡器旨在最小化总误差（ISI + 噪声），在有噪声的情况下通常性能更好。
- 两者都属于**线性均衡器**。

### 自适应线性均衡器 (Adaptive Linear Equalizer)

在信道特性未知或随时间变化时，均衡器系数需要能够自动调整，这就是自适应均衡。
- 最优系数向量可以通过迭代方法获得，例如**最速下降法 (steepest descent method)**。
- **最速下降法**:
  - 迭代更新规则: $\mathbf{x}_{k+1} = \mathbf{x}_k - \Delta \mathbf{g}_k$
  - $\mathbf{x}_k$ 是当前的参数向量，$\mathbf{g}_k$ 是在 $\mathbf{x}_k$ 处的梯度。
  - $\Delta$ 是步长，控制收敛速度和稳定性。

- **应用于MMSE均衡器**:
  - 目标函数是均方误差: $f(\mathbf{c}) = E[(z(mT)-a_m)^2]$
  - 梯度为: $\mathbf{g} = 2E[e_m \cdot \mathbf{y}(mT)]$，其中 $e_m=z(mT)-a_m$ 是瞬时误差，$\mathbf{y}(mT)$ 是均衡器输入向量。

- **LMS (Least Mean Square) 算法**:
  在实践中，用瞬时值的估计来代替梯度的期望值，得到梯度向量的估计：
  $$
  \hat{\mathbf{g}}_m = e_m \cdot \mathbf{y}(mT)
  $$
  系数更新法则变为：
  $$
  \mathbf{c}_{m+1} = \mathbf{c}_m - \Delta \cdot e_m \cdot \mathbf{y}(mT)
  $$
  这个简单的迭代过程就是著名的LMS算法。

![自适应线性均衡器结构图](https://raw.githubusercontent.com/Klender-J/Image-hosting/main/img/20240105001446.png)

### 更多关于均衡器的内容

均衡器可以根据不同标准进行分类：

- **根据工作方式**:
  - **预设式 (Preset Equalizer)**: 使用固定的训练序列进行初始设置。
  - **自适应式 (Adaptive Equalizer)**: 在数据传输过程中持续跟踪信道变化并调整系数。
  - **盲均衡 (Blind Equalizer)**: 无需训练序列，直接从接收信号中提取统计特性进行均衡。
- **根据结构**:
  - **线性 (Linear)**
    - **ZF**: 迫零
    - **MMSE**: 最小均方误差
  - **非线性 (Non-linear)**
    - **DFE (Decision Feedback Equalizer)**: 判决反馈均衡器
    - **MLSE (Maximum Likelihood Sequence Estimation)**: 最大似然序列估计

![均衡器分类](https://raw.githubusercontent.com/Klender-J/Image-hosting/main/img/20240105001452.png)