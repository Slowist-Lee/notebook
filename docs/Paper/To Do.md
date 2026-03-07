


---

# 🚀 LLM 推理能效深度研究路线图 (Integrated Roadmap)

**硬件环境**: 4x RTX 5090 | **目标**: 完成 Task 1-4 并输出高质量分析报告

---

## Phase 1: 基础构建与基准认知 (Setup & Baseline)

**目标**：跑通环境，并建立对“什么是正常能耗”的认知。


### 📚 理论准备

-  [x] **阅读 Paper 4 (Energy Efficient or Exhaustive?)**
    *   **目的**：了解 LLM 推理生命周期（Setup -> Token Gen）的能耗分解。
    *   *思考点*：论文中提到 GPU 占总能耗的比例是多少？这对你编写监控脚本（Task 2）关注哪些指标有指导意义。
- [x]  **阅读 Paper 5 (Words to Watts)**
    *   **目的**：查看 V100/A100 的历史数据，建立基准线。
    *   *思考点*：虽然你用的是 5090，但论文中“模型切分（Sharding）”对能耗的影响值得注意（如果你在多卡上跑）。

### 🛠️ 实践任务 (Task 1)

- [ ]  **环境搭建**：安装 vLLM，下载 Llama-3-8B-Instruct。
- [ ]  **冒烟测试**：
    *   准备 50 个 Prompts（涵盖长短输入）。
    *   成功运行一次推理，确保不报错。
    *   记录环境参数：Driver Version, CUDA Version, vLLM Version。

---

## Phase 2: 监控工具开发与底层逻辑探究 (Profiler & Internals)

**目标**：开发高精度测量工具，并理解 vLLM 内部是如何处理请求的。

### 💻 源码研读 (vLLM Deep Dive)
- [ ]  **核心任务：阅读 vLLM 调度逻辑**
    *   定位文件：`vllm/core/scheduler.py` 和 `vllm/engine/llm_engine.py`。
    *   **目的**：理解 vLLM 是如何将请求打包成 Batch 的（Continuous Batching）。
    *   *结合 Paper 7 (throttLL’eM)*：论文提到了 KV Cache 的增长会阻塞调度，看代码中是如何检查 `BlockSpace` 是否足够的。这对解释 Task 4b (Batch Size) 的结果至关重要。

### 🛠️ 实践任务 (Task 2)
- [ ]  **开发 `power_monitor.py`**
    *   **API 选择**：使用 `pynvml` (Python bindings for NVML) 而非 `nvidia-smi` 命令行调用（减少系统开销，提高采样率）。
    *   **采样频率**：设定为 **50ms**（为了捕捉 Prefill 瞬间的功耗尖峰）。
    *   **数据字段**：`Timestamp`, `Power (W)`, `GPU Util (%)`, `GPU Clock (MHz)`, **`Memory Util (%)`**(重要：用于后续分析 KV Cache)。
    *   **计算逻辑**：实现 `Total Energy (Joules)` 和 `Energy/Token` 的自动计算。

---

## Phase 3: 核心实验 A —— 阶段差异分析 (Prefill vs Decode)

**目标**：通过实验验证“计算密集”与“访存密集”的理论差异。

- [ ] 
### 📚 理论准备
- [ ]  **重点精读 Paper 1 (BiScale)**
    *   **核心概念**：Prefill 是 Compute-bound（计算受限），Decode 是 Memory-bound（带宽受限）。
    *   *指导意义*：这篇论文解释了为什么我们要把这两个阶段分开测。
    *   *预测*：Prefill 阶段 GPU 利用率和功耗应该接近 100%，而 Decode 阶段可能会低很多。

### 🛠️ 实践任务 (Task 3)
- [ ]  **Prefill 隔离测试**
    *   设置：`prompt_len = 2000`, `max_tokens = 1`。
    *   记录：峰值功率、持续时间。
- [ ]  **Decode 隔离测试**
    *   设置：`prompt_len = 10`, `max_tokens = 500`。
    *   记录：平均功率、持续时间。
- [ ]  **数据分析**
    *   绘制“功率-时间”曲线图。
    *   **关键分析**：使用 BiScale 的理论解释为什么 Decode 阶段 GPU 没有满载（算力闲置，等待显存搬运数据）。

---

## Phase 4: 核心实验 B —— 频率缩放与能效解耦 (DVFS)

**目标**：验证降低频率是否真的能在不牺牲性能的情况下省电。

### 📚 理论准备
- [ ]  **重点精读 Paper 6 (Providing load flexibility...)**
    *   **核心概念**：Energy-performance decoupling（能效-性能解耦）。
    *   *指导意义*：论文证明了在 Memory-bound 任务中，降低频率不会线性降低性能，但会显著降低功耗（因为功耗与频率的立方成正比，而性能只受显存带宽限制）。
- [ ]  **辅助阅读 Paper 7 (throttLL’eM)**
    *   *指导意义*：学习它是如何在迭代级别（Iteration-level）进行预测性降频的。

### 🛠️ 实践任务 (Task 4a)
- [ ]  **锁频实验**
    *   使用 `sudo nvidia-smi -lgc <freq>` 锁定频率。
    *   测试点：Max (e.g., 2500MHz), 80%, 60%, 40% (e.g., 800MHz)。
- [ ]  **对比分析**
    *   分别观察对 Prefill (Task 3 设置) 和 Decode (Task 3 设置) 的影响。
    *   **关键问题**：降低 30% 频率，Decode 的 TPS (Tokens/sec) 降低了多少？功耗降低了多少？如果 TPS 没怎么降但功耗大降，恭喜你复现了 Paper 6 的结论。
    *   寻找 **Sweet Spot**：画出 J/token 随频率变化的曲线，找到最低点。

---

## Phase 5: 核心实验 C —— 批处理效应 (Batch Size)

**目标**：探究大规模并发下的能效边界。

### 📚 理论准备
- [ ]  **阅读 Paper 2 (Patel et al. - Characterizing Power...)**
    *   **核心概念**：Power Oversubscription（功率超额认购）和 Inference Headroom（推理余裕）。
    *   *指导意义*：了解当 Batch Size 增大时，不同请求的计算峰值如何叠加，以及是否存在“功率墙”。
- [ ]  **回顾 Paper 5 (PagedAttention)**
    *   *指导意义*：理解 Batch Size 的上限是由显存（KV Cache）决定的，而非算力。

### 🛠️ 实践任务 (Task 4b)
- [ ]  **Batch Size 阶梯测试**
    *   脚本修改：使用 `vllm.LLM` 的 `generate` 接口同时发送 `[1, 2, 4, 8, 16, 32, 64, 128]` 个请求。
    *   监控：记录 GPU 显存占用率（验证 Paper 7 的 KV Cache 增长理论）和总功耗。
- [ ]  **数据分析**
    *   绘制 `J/token` vs `Batch Size` 曲线。
    *   **关键分析**：解释为什么 Batch Size 变大更省电？（提示：模型权重读取一次，服务多个请求 -> 均摊了显存带宽的能耗成本）。

---

## Phase 6: 综合报告与展示 (Presentation)

**目标**：将实验数据升华为理论洞察。

- [ ]  **架构图绘制**：参考 **Paper 3 (DynamoLLM)**，画出你的实验流程图（Input -> Engine -> Profiler -> Metrics）。
- [ ]  **核心结论串联**：
    *   *现象*：Decode 阶段降频能效提升显著。 -> *引用 Paper 6 (Decoupling)*。
    *   *现象*：Prefill 阶段降频导致延迟暴增。 -> *引用 Paper 1 (BiScale)*。
    *   *现象*：大 Batch Size 能效极高。 -> *引用 Paper 5 (vLLM/PagedAttention)*。
- [ ]  **绿色计算升华**：
    *   参考 **Paper 2 (Patel)**，计算如果该策略部署在数据中心，能节省多少电力成本。

---

**💡 为什么要保留 vLLM 源码阅读？**
在做 Task 4b（Batch Size）和 Task 3（Prefill/Decode）时，你会发现 vLLM 的调度器（Scheduler）在显存不足时会发生 **Preemption（抢占/换出）**。如果不读源码，你可能会看到实验数据中出现莫名的延迟尖峰而无法解释。Paper 7 (throttLL’eM) 正是针对这一点做了预测优化。读懂源码能让你解释实验中的“异常数据”。