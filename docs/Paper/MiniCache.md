## MiniCache: KV Cache Compression in Depth Dimension for Large Language Models

> Akide Liu, Jing Liu, Zizheng Pan, Yefei He, Gholamreza Haffari, Bohan Zhuang, From ZIP Lab

## 论文背景和问题

1. KV Caches
2. 疑似Baseline？： a 175B GPT-3 model [2], with a batch size of 64 and a sequence length of 4,096 tokens (both prefilled and generated), requires approximately 1,208GB of GPU memory

所以要进行KV Cache的compression.

目前的KV Cache的相关工作：KV Cache Evition / KV Cache Quantization

所以找层与层之间的关系，这篇工作做的是 KV Cache Merging：发现在整个模型后半部分，层间的 KV Cache 差异并不大，因此可以将多个层的 KV Cache 进行合并，从而减小 KV Cache 的存储占用

*   **原来的问题**：直接把两层的数据（向量）加起来求平均，精度损失会很大。
*   **作者的创新（重参数化）**：
    *   他们借鉴了“权重归一化（Weight Normalization）”的思想，把 KV Cache 中的**向量（Vector）** 拆成了两个部分：
        1.  **方向 (Direction)**：这个向量指向哪里？
        2.  **模长 (Magnitude)**：这个向量有多长？
*   **如何合并**：
    *   作者发现，层与层之间的**方向**通常很相似，但**模长**可能不同。
    *   所以，他们只对**方向**进行插值（混合/合并），把两层的方向变成一个方向存起来。
    *   同时，保留原始的**模长**（这是一个标量，占内存很小，所以保留下来不亏）。
*   **好处**：这就像在极坐标系里做插值，既节省了存方向向量的空间，又通过保留模长维持了原本的信息量。

*   **问题**：并不是所有的 Token 在不同层之间都很像。有一小部分 Token（离群点），它们在第 N 层和第 N+1 层差异巨大（相似度低），而且含义截然不同。
*   **后果**：如果强行把这些差异很大的 Token 合并，模型就会“变傻”，性能下降。
*   **解决办法**：
    *   挑出这些“刺头”（Unsuitable state pairs）。
    *   不对它们进行合并，而是**单独把它们完整地存下来**。
    *   **保留离群点**是为了防止性能崩盘。



论文背景和问题、论⽂动机和贡献解读、方案设计详细分析、 实验效果及其分析、结论、自己的思考

