
好的，我们将以您提供的两份课件（Chapter 5 和 Chapter 6）为大纲，结合您提供的历年考题和作业题，为您整理一份详尽的期末复习笔记。

本文档将严格按照知识点、题型整理、应试做题方法、历年真题及解析的结构进行组织，确保覆盖所有考点和题目。

***

### **Chapter 5: Large and Fast: Exploiting Memory Hierarchy (利用存储器层次结构：兼顾大与快)**

本章核心在于理解计算机如何通过构建存储器层次结构（Memory Hierarchy）来同时获得“像最快存储器一样快，像最慢存储器一样大”的访问效果。其理论基础是**局部性原理 (Principle of Locality)**。

---

### **第一部分：存储器层次结构基础 (Basics of Memory Hierarchy)**

#### **知识点 1: 局部性原理 (Principle of Locality)**

*   **核心思想**: 程序在一个时间段内访问的地址空间，通常只占其总地址空间的一小部分。这是构建存储器层次结构的理论基石。
*   **时间局部性 (Temporal Locality)**: 如果一个数据项被访问，那么在不久的将来它很可能再次被访问。
    *   **例子**: 循环中的指令、循环变量（如`for (i=0; ...)`中的`i`）。
*   **空间局部性 (Spatial Locality)**: 如果一个数据项被访问，那么与它地址相邻的数据项也很可能在不久的将来被访问。
    *   **例子**: 顺序执行的指令、数组元素的遍历。

#### **知识点 2: 存储器层次结构 (Memory Hierarchy)**

*   **目标**: 利用局部性原理，在不同速度、容量和成本的存储设备间取得平衡，为CPU提供一个容量大、速度快、成本低的“理想”存储系统。
*   **结构**: 一个层次结构，从上到下：
    1.  **CPU 寄存器 (Registers)**: 最快，最小，最贵。
    2.  **高速缓存 (Cache Memory - SRAM)**: 比寄存器慢，比主存快。
    3.  **主存储器 (Main Memory - DRAM)**: 比Cache慢，容量更大。
    4.  **二级存储 (Secondary Memory - Flash, Magnetic Disk)**: 最慢，最大，最便宜。
*   **工作原理**: 高层存储器作为低层存储器的一个**缓存 (Cache)**。数据以**块 (Block / Line)**为单位在不同层级之间复制。
    *   **命中 (Hit)**: CPU需要的数据在当前层（高层）存储器中找到。
        *   **命中率 (Hit Ratio)** = 命中次数 / 总访问次数
    *   **缺失 (Miss)**: CPU需要的数据不在当前层，需要从下一层（低层）调取。
        *   **缺失率 (Miss Ratio)** = 缺失次数 / 总访问次数 = 1 - 命中率
        *   **缺失代价 (Miss Penalty)**: 将数据从低层调入高层并送至CPU所需的时间。

#### **知识点 3: 存储技术 (Memory Technologies)**

*   **SRAM (静态随机访问存储器)**: 速度非常快 (0.5ns - 2.5ns)，但成本高，功耗大，密度低。通常用于构建**Cache**。
*   **DRAM (动态随机访问存储器)**: 速度比SRAM慢 (50ns - 70ns)，但成本低，功耗小，密度高。通常用于构建**主存**。
*   **Flash Memory (闪存)**: 非易失性存储，速度介于DRAM和磁盘之间。
*   **Magnetic Disk (磁盘)**: 速度最慢，但容量巨大，成本极低。

#### **题型整理与应试方法**

这类基础知识点主要以**选择题**和**判断题**形式考察对基本概念的理解。

**应试做题方法**:

1.  熟记时间局部性和空间局部性的定义和典型例子。
2.  理解存储器层次结构每一层的特点（速度、容量、成本）和常用技术（SRAM, DRAM）。
3.  掌握命中、缺失、命中率、缺失率、缺失代价等核心术语的含义。

---

#### **历年真题与解析**

**【选择题】**

> 1.  When performing a looping operation, the instruction gets stored in the`_____`. (2020-2021 P1)
>     A. Registers
>     B. Cache
>     C. System heap
>     D. System stack
>
> **答案**: B
> **解析**: 循环操作体现了**时间局部性**（指令被反复执行）。根据存储器层次结构原理，为加速访问，这些频繁执行的指令会被加载到Cache中。

> 2.  The main purpose of having memory hierarchy is to`_____`. (2018-2019 P70, P78)
>     A. Reduce access time
>     B. Provide large capacity
>     C. Reduce propagation time
>     D. Reduce access time & provide large capacity
>
> **答案**: D
> **解析**: 存储器层次结构的目标就是通过结合不同存储器的优点，对外提供一个既有高速度（类似Cache）又有大容量（类似磁盘）的存储系统。

> 3.  The L1 cache on a high-end processor is most likely to use which technology? (2018-2019 P70, P78)
>     A. flash
>     B. magnetic disk
>     C. SRAM
>     D. DRAM
>
> **答案**: C
> **解析**: L1 Cache是离CPU最近的高速缓存，对速度要求极高，因此使用速度最快的SRAM技术。

> 4.  The temporal aspect of the locality of reference means`_____`. (2017-2018 P61, 2010-2011 P111, 2023-2024 P122)
>     A. That the recently executed instruction won’t be executed soon
>     B. That the recently executed instruction will be executed soon again
>     C. That the recently executed instruction is temporarily not referenced
>     D. None of the mentioned
>
> **答案**: B
> **解析**: 时间局部性的定义就是最近访问过的数据项（或指令）很可能在不久的将来再次被访问。

> 5.  The fastest data access is provided using`_____`. (2017-2018 P61, 2010-2011 P113)
>     A. Caches
>     B. DRAMs
>     C. SRAMs
>     D. Registers
>
> **答案**: D
> **解析**: 在存储器层次结构中，CPU寄存器是速度最快的存储设备。

> 6.  The effectiveness of the cache memory is based on the property of`_____`. (2019-2020 P88)
>     A. Locality of reference
>     B. Memory localization
>     C. Memory size
>     D. None of the mentioned
>
> **答案**: A
> **解析**: Cache之所以有效，就是因为它利用了程序的局部性原理，将可能被频繁访问的数据预先存放在高速存储器中。

> 7. The reason for the implementation of the cache memory is`_____`. (2010-2011 P110, 2023-2024 P123)
>     A. to increase the internal memory of the system
>     B. the difference in speeds of operation of the processor and memory
>     C. to reduce the memory access and cycle time
>     D. all of the mentioned
>
> **答案**: B
> **解析**: 核心原因是CPU的速度远超主存（DRAM）的速度，存在巨大的速度鸿沟 (Processor-Memory Gap)。Cache (SRAM) 作为中间层，弥补了这个速度差异。

> 8. The SRAMs are basically used as`_____`. (2010-2011 P109)
>     A. register
>     B. cache
>     C. main memory
>     D. disk
>
> **答案**: B
> **解析**: SRAM因其高速特性，主要用于制造高速缓存 (Cache)。

> 9. The time delay between two successive initiations of memory operation is`_____`. (2020-2021 P1)
>     A. Instruction delay
>     B. Memory search time
>     C. Memory cycle time
>     D. Memory access time
>
> **答案**: C
> **解析**: **存储周期 (Memory cycle time)** 定义为连续两次独立的存储器操作（读或写）之间所需的最小时间间隔。它通常大于**存取时间 (Memory access time)**，因为存取时间只衡量一次操作的完成时间，而存储周期还包括存储器恢复到可以进行下一次操作状态的时间。

**【判断题】**

> 1.  Caches take advantage of temporal locality. (T/F) (2013-2014 P12)
>
> **答案**: T (True)
> **解析**: Cache同时利用了时间局部性（将最近访问的数据保留在Cache中）和空间局部性（一次调入一个数据块）。

> 2. The physical memory is not as large as the address space spanned by the processor. (T/F) (2018-2019 P72, P80)
>
> **答案**: T (True)
> **解析**: 这正是虚拟内存要解决的问题。例如，32位处理器可以寻址4GB空间，但物理内存（DRAM）通常远小于4GB。

> 3. The drawback of building a large memory with DRAM (Dynamic Random Access Memory) is`_____`. (2019-2020 P88)
>     A. The large cost factor
>     B. The inefficient memory organization
>     C. The Slow speed of operation
>     D. All of the mentioned
>
> **答案**: C
> **解析**: DRAM相对于CPU来说，主要缺点是速度慢，无法匹配CPU的运行速度，这是引入Cache的主要原因。

> 4. In the memory hierarchy, as the speed of operation increases the memory size also increases. (T/F) (2010-2011 P114, 2023-2024 P124)
>
> **答案**: F (False)
> **解析**: 关系恰好相反。在存储器层次结构中，速度越快，容量越小，成本越高。例如，寄存器比Cache快，但容量小得多。

---

### **第二部分：高速缓存 (Cache Memory)**

这是本章的考试重点，涵盖了Cache的组织结构、地址映射、性能计算、写策略等。

#### **知识点 1: Cache 地址映射与组织 (Address Mapping & Organization)**

CPU发出的内存地址需要被映射到Cache中。地址会被划分为三个部分：**标记 (Tag)**, **索引 (Index)**, **块内偏移 (Block Offset)**。

$$
\text{地址位数} = \text{Tag 位数} + \text{Index 位数} + \text{Offset 位数}
$$

*   **块内偏移 (Block Offset)**: 用于在Cache块中定位具体的字节/字。
    *   $$ \text{块大小 (Block Size)} = 2^{\text{Offset 位数}} \text{ 字节} $$
*   **索引 (Index)**: 用于确定内存块应该映射到Cache的哪一个**组 (Set)**。
    *   $$ \text{Cache 中的组数 (Number of Sets)} = 2^{\text{Index 位数}} $$
*   **标记 (Tag)**: 用于区分映射到同一个Cache组的不同内存块。

**Cache的三种映射方式**:

1.  **直接映射 (Direct Mapped)**
    *   **概念**: 每个内存块只能映射到Cache中的一个**固定**位置。
    *   **映射规则**: `(内存块地址) mod (Cache中的总块数)`
    *   **结构**: 每个索引对应一个Cache块（即每组只有1路）。
    *   **优点**: 实现简单，硬件成本低，查找速度快（只需比较1次Tag）。
    *   **缺点**: 冲突率高。如果两个频繁访问的内存块映射到同一个Cache行，会导致频繁的替换和抖动 (thrashing)，即使Cache还有很多空闲空间。

2.  **全相联映射 (Fully Associative)**
    *   **概念**: 任何内存块可以映射到Cache中的**任何**位置。
    *   **结构**: 整个Cache只有一个组，包含所有Cache块。地址中没有Index位。
    *   **优点**: 冲突率最低，Cache空间利用率最高。
    *   **缺点**: 实现复杂，硬件成本高（需要N个比较器，N为Cache总块数），查找速度慢。

3.  **组相联映射 (N-way Set Associative)**
    *   **概念**: 上述两种方式的折中。Cache被分成若干个组 (Set)，每个组内包含N个块 (Way)。
    *   **映射规则**: 内存块首先通过Index映射到一个**特定**的组，然后在该组内的**任何**位置存放。` (内存块地址) mod (Cache中的总组数)`
    *   **结构**: 直接映射是1-way组相联，全相联是 C/B -way组相联（C为Cache容量，B为块大小）。
    *   **优点**: 在冲突率和硬件成本之间取得了很好的平衡。
    *   **缺点**: 实现比直接映射复杂（需要N个比较器），但比全相联简单。

#### **题型一：Cache 参数计算**

这类题目会给出Cache的配置（容量、块大小、相联度、地址位数），要求计算Tag、Index、Offset的位数，或者反向推导。

**应试做题方法**:

1.  **计算块内偏移 (Offset) 位数**:
    $$ \text{Offset bits} = \log_2(\text{Block Size in bytes}) $$
    *注意：如果块大小是 W 个字，而一个字是4字节，那么块大小是 4W 字节。*

2.  **计算组数 (Number of Sets)**:
    $$ \text{Number of Sets} = \frac{\text{Cache Capacity}}{\text{Block Size} \times \text{Associativity (N-way)}} $$

3.  **计算索引 (Index) 位数**:
    $$ \text{Index bits} = \log_2(\text{Number of Sets}) $$

4.  **计算标记 (Tag) 位数**:
    $$ \text{Tag bits} = \text{Total Address bits} - \text{Index bits} - \text{Offset bits} $$

---

#### **历年真题与解析**

**【计算题型 - 选择题】**

> 1.  For a 32-bit cache-memory system, a 32KB, 4-way set-associative cache has 2 words cache line size, how many bits are there in such cache’s tag? (2020-2021 P2, 2013-2014 P19, 2015-2016 P38, 2017-2018 P62)
>     A: 19
>     B: 21
>     C: 23
>     D: 25
>
> **答案**: A
> **解析**:
> 1.  **求Offset位数**: Cache line size (块大小) = 2 words。RISC-V中1 word = 4 bytes。所以块大小 = 2 * 4 = 8 bytes。
>     $$ \text{Offset bits} = \log_2(8) = 3 \text{ bits} $$
> 2.  **求组数 (Number of Sets)**: Cache容量 = 32 KB = $$2^{15}$$ bytes。相联度 N = 4。
>     $$ \text{Number of Sets} = \frac{32 \times 1024}{8 \times 4} = \frac{2^{15}}{2^3 \times 2^2} = 2^{10} = 1024 \text{ sets} $$
> 3.  **求Index位数**:
>     $$ \text{Index bits} = \log_2(1024) = 10 \text{ bits} $$
> 4.  **求Tag位数**: 总地址位数 = 32 bits。
>     $$ \text{Tag bits} = 32 - 10 - 3 = 19 \text{ bits} $$

> 2.  Suppose you have a cache with capacity of 2¹⁵ bytes, with 32-byte blocks. Assume 8 bits are used to select the set. What is the associativity of the cache? (2018-2019 P70, P78)
>     A. The cache is direct-mapped.
>     B. The cache is two-way set associative.
>     C. The cache is four-way set associative.
>     D. None of the above.
>
> **答案**: C
> **解析**:
> 1.  **已知信息**: Cache容量 = $$2^{15}$$ bytes，块大小 = 32 bytes = $$2^5$$ bytes，Index位数 = 8 bits。
> 2.  **求组数 (Number of Sets)**:
>     $$ \text{Number of Sets} = 2^{\text{Index bits}} = 2^8 = 256 \text{ sets} $$
> 3.  **使用公式反推相联度 (N)**:
>     $$ \text{Number of Sets} = \frac{\text{Cache Capacity}}{\text{Block Size} \times N} $$
>     $$ 256 = \frac{2^{15}}{32 \times N} $$
>     $$ 2^8 = \frac{2^{15}}{2^5 \times N} = \frac{2^{10}}{N} $$
>     $$ N = \frac{2^{10}}{2^8} = 2^2 = 4 $$
>     所以，这是4-way组相联高速缓存。

> 3. For a memory unit of 512 kB, what’s the total size of address bits and data bits? (2020-2021 P1)
>     A. 17
>     B. 19
>     C. 27
>     D. 36
>
> **答案**: C
> **解析**:
> 1. **地址位 (Address bits)**: 存储单元是按字节寻址的。容量为 512 kB = 512 * 1024 bytes = $$2^9 \times 2^{10} = 2^{19}$$ bytes。所以需要 19 位地址线来寻址每一个字节 ($$ \log_2(2^{19}) = 19 $$)。
> 2. **数据位 (Data bits)**: 在没有特殊说明的情况下，一个存储单元（一个地址对应的数据）通常是 1 字节，即 8 位。
> 3. **总位数**: 地址位 + 数据位 = 19 + 8 = 27。

#### **题型二：Cache 访问过程追踪**

这类题目会给出一个Cache的配置和一串内存访问序列，要求判断每次访问是Hit还是Miss，并给出最终Cache的内容。

**应试做题方法**:

1.  **分析Cache结构**: 确定是哪种映射方式，计算出总块数或总组数。
2.  **计算映射位置**: 对于每次内存访问地址，计算它应该映射到哪个Cache块/组。
    *   **块地址 (Block Address)** = ` floor(内存字节地址 / 块大小)`
    *   **Cache索引 (Index)** = `块地址 mod Cache总块数/组数`
3.  **追踪访问**:
    *   **初始化**: Cache初始为空，所有Valid bit为0。
    *   **对每个地址**:
        a.  计算出Index。
        b.  查看对应Index的Cache行。
        c.  **判断Hit/Miss**:
            *   **直接映射**: 检查Valid位是否为1，且Tag是否匹配。
            *   **组相联**: 检查组内所有行的Valid位和Tag。
            *   **全相联**: 检查所有行的Valid位和Tag。
        d.  **更新Cache状态**:
            *   **Hit**: 不变。
            *   **Miss**: 将新的内存块调入。如果对应位置已有数据，则进行**替换**。如果是组相联或全相联，需要根据替换策略（如LRU）选择一个块来替换。

---

#### **历年真题与解析**

**【追踪题型 - 选择题】**

> 1.  For the following memory access pattern: 1,5,1,6,3, what’s the content of a 4-entries, direct-mapped cache, assuming cache is vacant at the beginning? (2020-2021 P3, 2013-2014 P19, 2015-2016 P40)
>
>     (The image shows four cache states, with option A having [empty, 3, 6, 1])
>
>     A. Correct
>     B. Incorrect
>     C. Incorrect
>     D. Incorrect
>
> **答案**: A
> **解析**:
> *   **Cache配置**: 直接映射，4个条目（块）。块大小未说明，默认按地址（块地址）访问。
> *   **映射规则**: `Index = 内存块地址 mod 4`
> *   **追踪过程**:
>     1.  **访问 1**: `1 mod 4 = 1`。Index=1处为空，Miss。Cache = Mem。
>     2.  **访问 5**: `5 mod 4 = 1`。Index=1处已有Mem，Tag不匹配，Miss。Cache = Mem。
>     3.  **访问 1**: `1 mod 4 = 1`。Index=1处是Mem，Tag不匹配，Miss。Cache = Mem。
>     4.  **访问 6**: `6 mod 4 = 2`。Index=2处为空，Miss。Cache = Mem。
>     5.  **访问 3**: `3 mod 4 = 3`。Index=3处为空，Miss。Cache = Mem。
> *   **最终状态**: Cache为空, Cache为Mem, Cache为Mem, Cache为Mem。题目选项中 `[empty, 3, 6, 1]` 的顺序可能是 `[c3, c2, c1, c0]` 或者 `[c0, c1, c2, c3]` 的变体，但内容是匹配的。

**【追踪题型 - 简答题】**

> 1.  Let A be a 1024×1024 matrix of 32-bit int elements stored in row-major order, aligned to the beginning of a cache line.
>     ```c
>     for (int i = 1; i < 16; i++) {
>         int x = A[0][i-1];
>         int y = A[i][i];
>         A[i][i] = x + y;
>     }
>     ```
>     Assume that memory accesses are executed in the order shown in the program. Variables x, y, and i are held in registers. Consider a 4 KiB direct-mapped L1 data cache with 16-byte cache lines. Assume that the cache is initially empty. The numbers of cache hits on the loop shown above is \_\_\_. (2023-2024 P5)
>     A. 16
>     B. 15
>     C. 14
>     D. 0
>
> **答案**: B
> **解析**:
> *   **Cache配置**:
>     *   容量 = 4 KiB = 4096 bytes。
>     *   块大小 = 16 bytes。
>     *   总块数 = 4096 / 16 = 256块。
>     *   直接映射，所以有256个组，每组1块。
>     *   Offset bits = log₂(16) = 4。
>     *   Index bits = log₂(256) = 8。
>     *   Tag bits = 32 - 8 - 4 = 20。
> *   **矩阵信息**:
>     *   `A`是 1024x1024 矩阵，每个元素4字节 (int)。
>     *   `A[i][j]`的地址 = `base_address + (i * 1024 + j) * 4`。
>     *   每行有 1024 * 4 = 4096 字节。
> *   **循环分析 (i 从 1 到 15)**:
>     *   `ld x, A[0][i-1]`: 读 `A[0][0]` 到 `A[0][14]`。
>     *   `ld y, A[i][i]`: 读 `A[1][1]`, `A[2][2]`, ..., `A[15][15]`。
>     *   `st A[i][i]`: 写 `A[1][1]`, `A[2][2]`, ..., `A[15][15]`。
> *   **追踪访问 `A[0][i-1]`**:
>     *   `i=1`: 读 `A[0][0]`。地址 `base + 0`。这是一个 compulsory miss。由于块大小为16字节，`A[0][0]` 到 `A[0][3]` (共4个整数) 被加载到同一个Cache块中。
>     *   `i=2`: 读 `A[0][1]`。地址 `base + 4`。这在 `i=1` 时已被加载，所以是 **Hit**。
>     *   `i=3`: 读 `A[0][2]`。地址 `base + 8`。**Hit**。
>     *   `i=4`: 读 `A[0][3]`。地址 `base + 12`。**Hit**。
>     *   `i=5`: 读 `A[0][4]`。地址 `base + 16`。Miss。加载 `A[0][4]` 到 `A[0][7]`。
>     *   总结 `A[0][i-1]` 的访问：每4次访问（对应一个16字节的块），有1次Miss和3次Hit。在`i`从1到15的15次循环中，`A[0][i-1]`被访问15次。
>         *   `i=1, 5, 9, 13` 时是 Miss (4次Miss)。
>         *   其余11次是 Hit。
> *   **追踪访问 `A[i][i]`**:
>     *   读 `A[1][1]`, `A[2][2]`, ... 这些元素地址相隔非常远。
>         *   `A[1][1]` 地址: `base + (1*1024 + 1)*4`
>         *   `A[2][2]` 地址: `base + (2*1024 + 2)*4`
>     *   地址间隔约为 1024*4 = 4096 字节，这正好是Cache的大小。
>     *   `Index = (address / 16) mod 256`。
>     *   `A[i][i]` 的地址 `(i*1024+i)*4`。
>     *   `A[i+1][i+1]` 的地址 `((i+1)*1024+i+1)*4 = (i*1024+i+1025)*4`。
>     *   地址差为 `1025 * 4 = 4100`。
>     *   块地址差为 `floor(4100/16) = 256`。
>     *   `Index(i+1) = (Index(i) + 256) mod 256 = Index(i)`。
>     *   这意味着所有的 `A[i][i]` 都映射到**几乎相同**的Cache索引。由于Tag不同，每次访问 `A[i][i]` 都会导致 Miss。所以读 `A[i][i]` 都是Miss。
> *   **追踪写 `A[i][i]`**:
>     *   写操作紧跟在读操作之后，访问的是同一个地址 `A[i][i]`。
>     *   由于读 `A[i][i]` 是Miss，会将包含 `A[i][i]` 的块加载到Cache中。
>     *   所以紧接着的写 `A[i][i]` 操作是 **Hit**。
>     *   `i`从1到15，共15次循环。因此，写 `A[i][i]` 会有15次Hit。
> *   **总计Hit数**:
>     *   来自 `A[0][i-1]` 的Hit: 11次。
>     *   来自写 `A[i][i]` 的Hit: 15次。
>     *   **错误分析**: 题目问的是整个循环中的Hit数。一次循环内有3次内存访问：`ld x`, `ld y`, `st A[i][i]`。
>     *   重新分析：
>         *   `i=1`: `ld A[0][0]` (Miss), `ld A[1][1]` (Miss), `st A[1][1]` (**Hit**).
>         *   `i=2`: `ld A[0][1]` (**Hit**), `ld A[2][2]` (Miss, 替换掉 `A[1][1]`), `st A[2][2]` (**Hit**).
>         *   `i=3`: `ld A[0][2]` (**Hit**), `ld A[3][3]` (Miss, 替换掉 `A[2][2]`), `st A[3][3]` (**Hit**).
>         *   `i=4`: `ld A[0][3]` (**Hit**), `ld A[4][4]` (Miss, 替换掉 `A[3][3]`), `st A[4][4]` (**Hit**).
>         *   `i=5`: `ld A[0][4]` (Miss, 但映射到不同块), `ld A[5][5]` (Miss), `st A[5][5]` (**Hit**).
>     *   `A[0][i-1]` 访问 (共15次):
>         *   Misses: i=1, 5, 9, 13 (4次)。
>         *   Hits: 15 - 4 = 11次。
>     *   `ld y, A[i][i]` 访问 (共15次):
>         *   如前分析，每次地址都不同且可能冲突，所以全部是 Miss (0次Hit)。
>     *   `st A[i][i]` 访问 (共15次):
>         *   每次写之前都刚刚发生了对同一地址的读Miss，该块已被加载。所以每次写都是 **Hit** (15次Hit)。
>     *   总Hit数 = 11 (from `ld x`) + 0 (from `ld y`) + 15 (from `st A[i][i]`) = 26次。
>     *   **再次审题和检查**: 让我们重新检查 `A[i][i]` 的冲突。
>       `A[i][i]`地址 `base + 4096*i + 4*i`。
>       `A[i+1][i+1]`地址 `base + 4096*(i+1) + 4*(i+1) = base + 4096*i + 4*i + 4096 + 4`。
>       地址差 `4100`。
>       `4100 = 16 * 256 + 4`。
>       这意味着`A[i+1][i+1]`的地址相对于`A[i][i]`的地址，在字节层面偏移了`4`，在块层面偏移了`256`个块。
>       `Index(A[i+1][i+1]) = floor( (Addr(A[i][i])+4100) / 16 ) mod 256`
>       `= floor( Addr(A[i][i])/16 + 4100/16 ) mod 256`
>       `= ( BlockAddr(A[i][i]) + 256 + 4/16 ) mod 256`
>       `= ( BlockAddr(A[i][i]) + 256 ) mod 256 = BlockAddr(A[i][i]) mod 256 = Index(A[i][i])`。
>       所以所有 `ld A[i][i]` 确实映射到同一个Index，每次都导致冲突Miss。
>       计算结果 26 仍然是正确的。但是选项里没有26。
>       **可能理解有误，重新思考**。
>       `A[0][i-1]` 访问：`i=1..15`, 访问 `A[0][0]` 到 `A[0][14]`。
>       - `i=1,..,4` 访问 `A[0][0]..A[0][3]`: 1 Miss, 3 Hits.
>       - `i=5,..,8` 访问 `A[0][4]..A[0][7]`: 1 Miss, 3 Hits.
>       - `i=9,..,12` 访问 `A[0][8]..A[0][11]`: 1 Miss, 3 Hits.
>       - `i=13,14,15` 访问 `A[0][12]..A[0][14]`: 1 Miss, 2 Hits.
>       - 总计：4 Misses, 11 Hits。这部分没问题。
>       `A[i][i]` 访问 `(ld` 和 `st)`：
>       - 每次 `ld A[i][i]` 都是 Miss。
>       - 每次 `st A[i][i]` 都是 Hit。
>       - 这部分总共有 15 Hits.
>       - 总计还是 11+15 = 26 Hits.
>       **换一个思路**。会不会题目有歧义？"the numbers of cache hits on the loop" 是指 `ld` 操作的 hit 还是所有操作的 hit？通常指所有数据访问。
>       也许 `A[0][i-1]` 和 `A[i][i]` 之间会互相冲突？
>       - `Addr(A[0][j]) = base + 4*j`. `BlockAddr = floor(j/4)`. `Index = floor(j/4) mod 256`. `A[0][0..14]` 的 `j` 很小，Index也很小。
>       - `Addr(A[i][i]) = base + 4096*i + 4*i`. `BlockAddr = 256*i + floor(i/4)`. `Index = (256*i + floor(i/4)) mod 256 = floor(i/4) mod 256`.
>       - 当 `i` 和 `j` 满足 `floor(j/4) = floor(i/4)` 时，它们映射到同一个 Index。
>       - `j=i-1`。所以 `Index(A[0][i-1]) = floor((i-1)/4)`。 `Index(A[i][i]) = floor(i/4)`。
>       - 当 `i` 不是4的倍数时, `floor((i-1)/4) == floor(i/4)`。
>         - `i=1`: `Index(A[0][0])=0`, `Index(A[1][1])=0` -> 冲突！
>         - `i=2`: `Index(A[0][1])=0`, `Index(A[2][2])=0` -> 冲突！
>         - `i=3`: `Index(A[0][2])=0`, `Index(A[3][3])=0` -> 冲突！
>         - `i=4`: `Index(A[0][3])=0`, `Index(A[4][4])=1` -> 不冲突！
>       - **重新追踪**:
>         *   `i=1`: `ld A[0][0]`(M), `ld A[1][1]`(M, 替换`A[0][0]`), `st A[1][1]`(H). **1 Hit**
>         *   `i=2`: `ld A[0][1]`(M, 替换`A[1][1]`), `ld A[2][2]`(M, 替换`A[0][1]`), `st A[2][2]`(H). **1 Hit**
>         *   `i=3`: `ld A[0][2]`(M, 替换`A[2][2]`), `ld A[3][3]`(M, 替换`A[0][2]`), `st A[3][3]`(H). **1 Hit**
>         *   `i=4`: `ld A[0][3]`(M, 替换`A[3][3]`), `ld A[4][4]`(M, 不冲突), `st A[4][4]`(H). **1 Hit**
>         *   `i=5`: `ld A[0][4]`(M, 不冲突), `ld A[5][5]`(M, 替换`A[4][4]`), `st A[5][5]`(H). **1 Hit**
>       - 看起来，每次循环 `ld A[0][i-1]` 都是Miss，因为它在前一次循环被 `ld A[i-1][i-1]` 替换掉了（除了 `i=4,8,12` 的边界情况）。
>       - `ld A[i][i]` 总是Miss。
>       - `st A[i][i]` 总是Hit。
>       - 这样总共就是 **15 Hits**。
>       - 我们来验证 `i=4` 的情况：`Index(A[0][3])=0`, `Index(A[4][4])=1`。
>         - `i=3` 结束后, Index 0 存的是 `A[3][3]` 的块。
>         - `i=4` 开始: `ld A[0][3]` (M, Index 0 被 `A[0][0-3]` 块覆盖), `ld A[4][4]` (M, 存入 Index 1), `st A[4][4]` (H).
>       - 我们来验证 `i=5` 的情况：`Index(A[0][4])=1`, `Index(A[5][5])=1`。
>         - `i=4` 结束后, Index 0 存 `A[0][0-3]` 块, Index 1 存 `A[4][4]` 块。
>         - `i=5` 开始: `ld A[0][4]` (M, Index 1 被 `A[0][4-7]` 块覆盖), `ld A[5][5]` (M, Index 1 被 `A[5][5]` 块覆盖), `st A[5][5]` (H).
>       - **最终结论**: `ld A[0][i-1]` 总是Miss, `ld A[i][i]` 总是Miss, `st A[i][i]` 总是Hit。总共15次循环，每次循环贡献1个Hit，总共 **15 Hits**。

#### **知识点 2: 写策略 (Write Policies)**

当发生写命中 (Write Hit) 时，如何处理数据更新？

1.  **写直通 (Write-Through)**:
    *   **操作**: 同时更新Cache和主存中的数据。
    *   **优点**: 实现简单，Cache和主存始终保持一致。
    *   **缺点**: 速度慢，因为每次写操作都要访问慢速的主存。需要**写缓冲 (Write Buffer)**来缓解CPU等待，CPU将数据写入Buffer后可立即继续执行，由Buffer负责将数据写入主存。
2.  **写回 (Write-Back / Copy-Back)**:
    *   **操作**: 只更新Cache中的数据，并设置一个**脏位 (Dirty Bit)**为1，表示该Cache块已被修改。直到这个脏块被替换出Cache时，才把它写回主存。
    *   **优点**: 速度快，多次写同一个块只需一次主存访问（在最后被替换时）。减少了总线带宽占用。
    *   **缺点**: 实现复杂，需要维护Dirty Bit。存在Cache和主存数据不一致的时期。

当发生写缺失 (Write Miss) 时，如何处理？

1.  **写分配 (Write Allocate / Fetch on Write)**:
    *   **操作**: 先把对应的内存块读入Cache，然后再执行写操作。
    *   **策略**: 通常与**写回**策略配合使用，因为它利用了后续可能对该块其他数据的读/写访问的局部性。
2.  **非写分配 (No-Write Allocate / Write Around)**:
    *   **操作**: 不把内存块读入Cache，直接把数据写入主存。
    *   **策略**: 通常与**写直通**策略配合使用。适用于初始化大块内存等场景，因为程序可能在读之前写满整个块。

#### **题型整理与应试方法**

主要考察对四种策略组合的理解，以**选择题**和**判断题**为主。

**应试做题方法**:

*   **写直通**: 关键词是 "also update memory", "consistent"。
*   **写回**: 关键词是 "dirty bit", "update only cache", "write back when replaced"。
*   **写分配**: 关键词是 "fetch the block on miss"。
*   **非写分配**: 关键词是 "don't fetch", "write directly to memory"。
*   **组合**: 写回通常搭配写分配，写直通通常搭配非写分配。

---

#### **历年真题与解析**

**【选择题】**

> 1.  The bit used to signify that the cache location is updated is`_____`. (2019-2020 P86)
>     A. Dirty bit
>     B. Update bit
>     C. Reference bit
>     D. Flag bit
>
> **答案**: A
> **解析**: Dirty bit (脏位) 用于标记一个Cache块是否被修改过，这是写回策略的核心。

> 2.  In`_____`__ protocol the data is directly written into the main memory. (2021-2022 P95, P103)
>     A. Write through
>     B. Write back
>     C. Write first
>     D. Write allocate
>
> **答案**: A
> **解析**: 写直通 (Write-through) 策略要求写操作同时更新Cache和主存。题目描述的“directly written into the main memory”正是其特点。
> *注意：虽然题目选项中没有“Write-through”，但从问题描述来看，应该是选项笔误，实际想考察的是写直通。如果必须从现有选项选，A最接近。如果是“Write first”这个不规范的术语，也可能指先写主存。但标准术语是Write-through。题目给的答案是C，这可能是某个特定教材的非标准术语，但在标准教材中应为Write-through。此处我们按标准理解，选择A。*

> 3. The copy-back protocol is used`_____`. (2010-2011 P110)
>     A. to copy the contents of the memory onto the cache
>     B. to update the contents of the memory from the cache
>     C. to remove the contents of the cache and push it on to the memory
>     D. none of the mentioned
>
> **答案**: B
> **解析**: Copy-back 是 Write-back (写回) 的别名。它的核心操作是在脏块被替换时，将Cache中的内容写回（更新）到主存中。

**【判断题】**

> 1.  A write-through cache typically requires more bus bandwidth than a write-back cache. (T/F) (2020-2021 P4, 2023-2024 P124 - with reversed logic)
>
> **答案**: T (True)
> **解析**: 写直通每次写操作都会访问主存，占用总线带宽。而写回只有在脏块被替换时才访问主存，如果一个块被多次写入，则大大节省了带宽。

> 2.  On every store instruction, a write-back cache will write to main memory. (T/F) (2015-2016 P42)
>
> **答案**: F (False)
> **解析**: 这是写直通的特点。写回策略只在脏块被替换时才写回主存。

> 3.  Write-through: A scheme that handles writes by updating values only to the block in the cache, then writing the modified block to the lower level of the hierarchy when the block is replaced. (T/F) (2018-2019 P72)
>
> **答案**: F (False)
> **解析**: 描述的是写回 (Write-back) 策略。写直通是同时更新Cache和主存。

> 4.  When meeting cache misses, “no write allocate” means only writing to main memory. (T/F) (2019-2020 P89)
>
> **答案**: T (True)
> **解析**: 非写分配 (No-write allocate) 策略在发生写缺失时，不加载数据块到Cache，而是直接将数据写入主存。

> 5. If a data cache does not contain a dirty bit, then it must be using a write-through policy. (T/F) (2019-2020 P89)
>
> **答案**: T (True)
> **解析**: Dirty bit是写回策略的必要组成部分，用于追踪哪些块被修改过。如果一个Cache没有脏位，它就无法实现写回，因此必须使用写直通策略。

#### **知识点 3: Cache 性能评估**

*   **CPU 时间 (CPU Time)** = (CPU 执行周期数 + 存储器停顿周期数) × 时钟周期时间
*   **存储器停顿周期数 (Memory Stall Cycles)** = 访存次数 × 缺失率 × 缺失代价
    *   或者 = 指令数 × (每条指令的缺失次数) × 缺失代价
*   **每条指令的平均访存次数 (AMAT per instruction)**: 对于RISC-V，每条取指指令访问1次指令存储器，Load/Store指令额外访问1次数据存储器。
*   **平均访存时间 (Average Memory Access Time, AMAT)**: 衡量存储系统性能的关键指标。
    $$ \text{AMAT} = \text{Hit Time} + \text{Miss Rate} \times \text{Miss Penalty} $$
    *   **Hit Time**: 访问Cache命中所需时间。
    *   **Miss Penalty**: 发生Cache miss的额外开销。

#### **题型三：Cache 性能计算**

这类题目会给出CPU、Cache、主存的各项性能参数（如CPI, 时钟频率, 命中率, 命中时间, 缺失代价等），要求计算AMAT、总CPI、性能提升等。

**应试做题方法**:

1.  **分清I-cache和D-cache**: 题目可能分别给出指令Cache和数据Cache的参数。计算总停顿时要分别计算两者的停顿周期然后相加。
    *   `I-cache stall = I-count * I-miss_rate * miss_penalty`
    *   `D-cache stall = (Load/Store count) * D-miss_rate * miss_penalty`
2.  **套用公式**: 准确理解每个参数的含义，套用AMAT或CPU时间的公式。
    *   `Actual CPI = Base CPI + Memory Stalls per Instruction`
    *   `Memory Stalls per Instruction = (Misses per Instruction) * Miss Penalty`
3.  **单位换算**: 注意时间和周期的换算。 `Miss Penalty (cycles) = Miss Penalty (time) / Clock Cycle Time`。

---

#### **历年真题与解析**

**【性能计算题型 - 选择题】**

> 1.  In a cache-memory system, assume that hit rate is 95％, and penalty to access the cache and main memory to be 1ns and 10ns respectively. We can infer that the average memory access time is`_____` ns. (2020-2021 P2)
>     A: (1＋10) / 2
>     B: 10×5%＋1×95%
>     C: (10＋1)×5%＋1×95%
>     D: 10×95%＋1×5%
>
> **答案**: B
> **解析**:
> *   题目中的 "penalty to access the cache" 指的是命中时间 (Hit Time) = 1ns。
> *   "penalty to access the main memory" 指的是从主存获取数据的时间。这里可以理解为缺失代价 (Miss Penalty)。但AMAT公式中的Miss Penalty是**额外**时间。更严谨的说法是：主存访问时间是10ns。
> *   我们有两种理解方式，但结果相同：
>     1.  `AMAT = Hit Time * Hit Rate + Miss Time * Miss Rate`
>         `= 1 * 95% + 10 * 5%`
>         `= 0.95 + 0.5 = 1.45 ns`
>     2.  `AMAT = Hit Time + Miss Rate * Miss Penalty`
>         `Miss Penalty` 是指发生缺失后，从开始确定缺失到数据返回的**额外**时间。如果主存访问时间是10ns，命中时间是1ns，那么缺失代价是 `10 - 1 = 9ns`。
>         `AMAT = 1 + 5% * 9 = 1 + 0.45 = 1.45 ns`。
> *   选项B的表达式是 `10 * 5% + 1 * 95%`，这与第一种计算方式吻合。

> 2.  Calculate AMAT (Average Memory Access Time) for a machine with the following specs: L1 cache with hit time = 1 cycle and miss rate = 5%, L2 cache with hit time = 5 cycles, miss rate = 15% and miss penalty = 200 cycles. (计组期末考试A P4)
>     A. 2.75 cycles
>     B. 2 cycles
>     C. 1.665 cycles
>     D. None of the above.
>
> **答案**: A
> **解析**:
> *   这是一个多级Cache的AMAT计算。L1的缺失代价 (Miss Penalty) 就是访问L2的时间。
> *   `AMAT_L2 = Hit_Time_L2 + Miss_Rate_L2 * Miss_Penalty_L2`
>     *   这里的 `Miss_Rate_L2` 是**局部缺失率 (Local Miss Rate)**。
>     *   `Miss_Penalty_L2` 是L2缺失后访问主存的代价 = 200 cycles。
>     *   `AMAT_L2 = 5 + 15% * 200 = 5 + 30 = 35` cycles。
> *   `AMAT_Total = Hit_Time_L1 + Miss_Rate_L1 * AMAT_L2`
>     *   `AMAT_Total = 1 + 5% * 35 = 1 + 1.75 = 2.75` cycles。

#### **知识点 4: 改进 Cache 性能的途径**

*   **降低缺失率 (Reducing Miss Rate)**
    1.  **增大块大小 (Larger Block Size)**: 利用空间局部性，减少强制性缺失。但过大的块会增加缺失代价，并可能因为“污染”而增加冲突缺失。
    2.  **增大Cache容量 (Larger Cache Size)**: 减少容量缺失。但会增加命中时间和成本。
    3.  **提高相联度 (Higher Associativity)**: 减少冲突缺失。但会增加命中时间和硬件复杂度。
*   **降低缺失代价 (Reducing Miss Penalty)**
    1.  **使用多级缓存 (Multilevel Caches)**: L1 miss后访问快速的L2，而不是慢速的主存。
    2.  **读缺失优先于写 (Read Priority over Write)**: 在写缓冲满时，优先处理读缺失，因为CPU通常在等待读结果。
*   **降低命中时间 (Reducing Hit Time)**
    1.  **使用更小的、简单的Cache**: 小容量、直接映射的Cache通常命中时间更短。

**3C Misses (缺失的三种分类)**

1.  **强制性缺失 (Compulsory Miss / Cold Start Miss)**: 第一次访问一个块时，由于Cache初始为空，必然发生的缺失。
2.  **容量缺失 (Capacity Miss)**: 由于Cache容量有限，无法容纳程序需要的所有块，导致被替换出去的块在之后被再次访问时发生的缺失。
3.  **冲突缺失 (Conflict Miss / Collision Miss)**: 在组相联或直接映射Cache中，多个内存块映射到同一个组（或行），即使Cache有空闲空间，也会因为目标组已满而发生替换，导致的缺失。

#### **题型整理与应试方法**

考察对各种优化手段及其副作用（trade-offs）的理解，以及对3C缺失的区分。通常是**选择题**和**判断题**。

**应试做题方法**:

*   记住每种优化方法的优缺点。例如：增大块大小 -> 降强制缺失，但可能增冲突缺失和缺失代价。
*   记住3C缺失的定义。
    *   全相联Cache只有强制性缺失和容量缺失，**没有冲突缺失**。
    *   增加相联度主要就是为了**减少冲突缺失**。

---

#### **历年真题与解析**

**【选择题】**

> 1. Which of the following cache designer guideline is not valid? (2020-2021 P3)
>     A. Fully associative caches have no conflict misses.
>     B. In reducing misses, associativity is more important than capacity.
>     C. The higher the memory bandwidth, the larger the cache block.
>     D. The shorter the memory latency, the smaller the cache block.
>
> **答案**: B
> **解析**:
> A. 正确。全相联允许块放在任何位置，消除了“抢位置”的冲突。
> B. 错误。通常来说，增加容量对降低缺失率的影响比增加相联度更显著，尤其是在Cache容量较小时。
> C. 正确。高带宽意味着可以快速传输一个大块，因此可以容忍大块带来的较长传输时间，从而更好地利用空间局部性。
> D. 正确。低延迟意味着取一个块很快，所以不需要一次取一个很大的块来摊销延迟成本，小块可以减少污染。

> 2. You want to maximize the performance of an application with the following characteristics: large number of data structures, low spatial locality, high temporal locality including frequent loads and stores to the same variable, 50% of the memory accesses are stores. Assuming a fixed total cache size, which set of choices below would most likely lead to increased performance? (2015-2016 P37, 2017-2018 P62)
>     A. Small block size, High associativity, LRU replacement, Write back, Write allocate
>     B. Large block size, Low associativity, LRU replacement, Write back, Write allocate
>     C. Small block size, High associativity, MRU replacement, Write through, No write allocate
>     D. Large block size, Low associativity, LRU replacement, Write through, Write allocate
>
> **答案**: A
> **解析**:
> *   **Low spatial locality**: 意味着访问地址不连续，大块没用，反而会带来污染。应选择 **Small block size**。
> *   **Large number of data structures**: 不同的数据结构可能会映射到相同的Cache组，导致冲突。应选择 **High associativity** 来降低冲突缺失。
> *   **High temporal locality**: 意味着数据会被反复访问，LRU (Least Recently Used) 是利用时间局部性的有效替换策略。
> *   **Frequent loads and stores to the same variable, 50% stores**: 频繁的写操作，特别是对同一变量，用 **Write back** 策略可以显著减少主存访问次数，性能更好。写回通常搭配 **Write allocate**。
> *   综合以上，A是最佳选择。

> 3. Increasing associativity can reduce`_____`. (2015-2016 P40, 2018-2019 P71, P79)
>     A. Compulsory misses (cold-start misses)
>     B. Capacity misses
>     C. Conflict misses (collision misses)
>     D. All three misses
>
> **答案**: C
> **解析**: 增加相联度提供了更多的块放置选择，直接目的就是为了减少因多个块映射到同一位置而产生的冲突缺失。

**【判断题】**

> 1.  First-level caches are more concerned about hit time, and second-level caches are more concerned about miss rate. (T/F) (2013-2014 P12, 2014-2015 P28, 2015-2016 P40)
>
> **答案**: T (True)
> **解析**: L1 Cache每次访存都要访问，其命中时间直接影响CPU时钟周期，因此必须快。L2 Cache的作用是处理L1的缺失，其目标是尽可能避免访问更慢的主存，因此降低缺失率是首要任务。

> 2. Fully associative caches have no conflict misses. (T/F) (2013-2014 P12)
>
> **答案**: T (True)
> **解析**: 定义。全相联映射消除了冲突。

> 3.  Bigger cache blocks always lead to a higher hit rate. (T/F) (2015-2016 P42, 2017-2018 P64)
>
> **答案**: F (False)
> **解析**: 增大块大小在一定程度上可以利用空间局部性降低缺失率，但如果块过大，而程序空间局部性不强，会导致不相关的数据被载入Cache（污染），反而可能因为块总数减少而增加冲突，导致缺失率上升。

> 4.  Adding a lower level cache reduces miss penalty. (T/F) (2016-2017 P49, P55)
>
> **答案**: T (True)
> **解析**: L1的缺失代价原本是访问主存的时间。增加了L2后，L1的缺失代价变成了访问L2的时间，这远小于访问主存的时间。

> 5.  Increasing set associativity increases hit time. (T/F) (2016-2017 P49, P55)
>
> **答案**: F (False) -> **这是一个有争议的点**
> **严格来说，答案是 T (True)**。因为更高的相联度意味着需要更多的比较器并行比较Tag，并且需要一个更复杂的多路选择器来选择数据，这会增加电路延迟，从而可能增加命中时间或延长CPU时钟周期。
> **但在某些课程的简化模型中，可能认为命中时间不变**。考试时需根据授课老师的强调来判断。从硬件实现角度，此说法为**真**。给出的答案是F，可能是因为在宏观性能模型计算中，通常将Hit Time视为一个固定值，而不考虑相联度对其微小的影响。

> 6.  The directly mapped cache no replacement algorithm is required. (T/F) (2018-2019 P72, P80)
>
> **答案**: T (True)
> **解析**: 直接映射中，每个内存块只有一个固定的映射位置。当发生冲突时，没有选择，只能替换掉当前位置的旧块。因此不需要复杂的替换算法（如LRU, FIFO）。

> 7. There is no way to reduce compulsory misses. (T/F) (2010-2011 P114, 2023-2024 P124 - with reversed logic)
>
> **答案**: F (False)
> **解析**: 虽然强制性缺失不可避免，但可以通过**预取 (Prefetching)** 技术来减少其影响。另外，增大块大小也可以减少强制性缺失的**次数**（因为一次性取了更多的数据）。

---

### **第三部分：虚拟内存 (Virtual Memory)**

虚拟内存将主存(DRAM)作为二级存储(Disk)的高速缓存，实现了地址空间的扩展和内存保护。

#### **知识点 1: 虚拟内存基本概念**

*   **目标**:
    1.  **扩展地址空间**: 允许程序使用比物理内存更大的地址空间。
    2.  **内存保护**: 每个进程拥有独立的虚拟地址空间，防止进程间相互干扰。
    3.  **内存管理**: 简化链接、加载和共享内存。
*   **核心机制**: 地址翻译 (Address Translation)。CPU生成**虚拟地址 (Virtual Address)**，通过硬件(MMU)和操作系统(OS)协作，将其转换为**物理地址 (Physical Address)**。
*   **术语对比**:

| Cache     | Virtual Memory   |
| :-------- | :--------------- |
| Block (块) | Page (页)         |
| Miss (缺失) | Page Fault (页缺失) |

#### **知识点 2: 页表 (Page Table)**

*   **功能**: 存储虚拟页号 (VPN) 到物理页号 (PPN) 的映射关系。
*   **结构**: 一个由**页表项 (Page Table Entry, PTE)** 组成的数组，存放在**主存**中。CPU中的**页表基址寄存器 (Page Table Base Register)** 指向当前进程页表的起始物理地址。
*   **地址翻译过程**:
    1.  CPU发出虚拟地址，分为**虚拟页号 (VPN)** 和**页内偏移 (Page Offset)**。
    2.  硬件使用VPN作为索引，在页表中查找对应的PTE。
        *   地址 = `页表基址寄存器值 + VPN * PTE大小`
    3.  从PTE中取出物理页号 (PPN)。
    4.  物理地址 = `PPN` + `Page Offset`。

#### **知识点 3: 加速地址翻译 - TLB**

*   **问题**: 每次访存都需要先访问主存中的页表，使得总访存次数加倍，性能急剧下降。
*   **解决方案**: **旁路转换缓冲 (Translation Look-aside Buffer, TLB)**。
    *   **本质**: 一个专门用于缓存**近期使用过的PTE**的高速缓存 (Cache)。
    *   **工作流程**:
        1.  CPU发出虚拟地址，硬件首先在TLB中查找VPN。
        2.  **TLB Hit**: 快速从TLB中获取PPN，完成地址翻译。
        3.  **TLB Miss**:
            a.  硬件或软件(OS)访问主存中的页表，找到对应的PTE。
            b.  将该PTE加载到TLB中（可能需要替换旧条目）。
            c.  重新执行指令。
*   **页缺失 (Page Fault)**: 如果在访问页表时，发现PTE中的有效位为0，表示该页不在主存中。此时会触发一个**异常 (Exception)**，控制权交给操作系统。
    *   **OS处理流程**:
        1.  在磁盘上找到该页。
        2.  在主存中找一个空闲物理页，若没有则根据替换算法（如LRU近似算法）选择一个牺牲页。
        3.  若牺牲页是脏的（被修改过），则先将其写回磁盘。
        4.  将目标页从磁盘读入物理页。
        5.  更新页表，将PTE指向新的物理页并设置有效位。
        6.  返回到原指令，重新执行。

#### **题型四：TLB/Cache/Page Fault 综合**

考察对整个访存流程的理解，即TLB、Cache、页表如何协同工作。

**应试做题方法**:

*   **牢记访存顺序**:
    1.  CPU发出虚拟地址。
    2.  **查TLB**:
        *   TLB Hit -> 得到物理地址 -> **查Cache**
        *   TLB Miss -> **查页表(在主存中)**
            *   Page Hit (页在主存) -> 更新TLB -> 得到物理地址 -> **查Cache**
            *   Page Fault (页在磁盘) -> OS处理 -> 更新页表和TLB -> 得到物理地址 -> **查Cache**
*   **分析各种组合**:
    *   `TLB Hit, Cache Hit`: 最快情况。
    *   `TLB Hit, Cache Miss`: 物理地址已知，但数据不在Cache，需从主存取。
    *   `TLB Miss, Page Hit, Cache Hit`: 罕见但可能。页表在主存，数据却在Cache（物理地址Cache）。
    *   `TLB Miss, Page Hit, Cache Miss`: 标准的TLB Miss处理流程。
    *   `TLB Miss, Page Fault`: 最慢情况，需要访问磁盘。

---

#### **历年真题与解析**

**【选择题】**

> 1.  `_____` is generally used to increase the apparent size of physical memory. (2020-2021 P1)
>     A. Secondary memory
>     B. Virtual memory
>     C. Hard disk
>     D. Disk
>
> **答案**: B
> **解析**: 虚拟内存技术使得程序认为自己拥有连续且巨大的内存空间，这个空间可以远大于实际的物理内存，从而“增加”了可用内存的表观大小。

> 2.  Which of the following situation will not happen? (2014-2015 P29, 2016-2017 P48, P55, 2018-2019 P71, P79)
>     A: TLB miss, Cache miss, Page miss
>     B: TLB miss, Cache hit, Page hit
>     C: TLB hit, Cache hit, Page miss
>     D: TLB hit, Cache miss, Page miss
>
> **答案**: C
> **解析**: Page Miss (页缺失) 意味着数据不在物理内存中。而Cache是物理内存的缓存，如果数据连物理内存都不在，它**绝对不可能**在Cache中。因此，Page Miss必然导致Cache Miss。`Cache hit` 和 `Page miss` 是互斥的。

> 3. For a virtual memory with translation look-aside buffer (TLB), which of following will be run first during memory access? (2017-2018 P60)
>     A. test cache hit
>     B. test TLB hit
>     C. test physical memory hit
>     D. test dirty bit
>
> **答案**: B
> **解析**: 地址翻译是访存的第一步。CPU生成虚拟地址后，必须先通过TLB（或页表）将其转换为物理地址，然后才能用物理地址去访问Cache或主存。

> 4. A page fault occurs when`_____`. (2023-2024 P123)
>     A. there is an error in a specific page
>     B. a program accesses a page of main memory
>     C. a program accesses a page not currently in main memory
>     D. a program accesses a page belonging to another program
>
> **答案**: C
> **解析**: 页缺失的定义就是程序试图访问一个虚拟页，但该页当前并未被加载到物理主存中。

> 5. A multilevel page table is preferred in comparison to a single level page table for translating virtual address to physical address because\_\_\_\_\_\_. (计组期末考试A P3)
>    A. it reduces the memory access time to read or write a memory location
>    B. it helps to reduce the size of page table needed to implement the virtual address space of a process
>    C. it is required by the translation lookaside buffer
>    D. it helps to reduce the number of page faults in page replacement algorithms
>
> **答案**: B
> **解析**: 对于一个大的虚拟地址空间，单级页表本身可能非常巨大（例如32位地址空间，4KB页，需要4MB页表）。多级页表通过只为实际使用的地址范围分配二级或更低级的页表来节省空间。

> 6. Assume a machine has 32-bit virtual address, 8 KiB page size, and 4-byte page table entry. What is the maximum possible page table size for a system running five processes? (2021-2022 P5)
>    A. 2 MiB
>    B. 5 MiB
>    C. 10 MiB
>    D. 20 MiB
>
> **答案**: C
> **解析**:
> 1.  **计算单个进程的页表大小**:
>     *   页大小 = 8 KiB = $$2^{13}$$ bytes.
>     *   虚拟地址空间 = $$2^{32}$$ bytes.
>     *   虚拟页数 = (虚拟地址空间大小) / (页大小) = $$2^{32} / 2^{13} = 2^{19}$$.
>     *   页表项 (PTE) 大小 = 4 bytes.
>     *   单个页表大小 = (虚拟页数) * (PTE大小) = $$2^{19} \times 4 = 2^{19} \times 2^2 = 2^{21}$$ bytes.
>     *   $$2^{21}$$ bytes = 2 * $$2^{20}$$ bytes = 2 MiB.
> 2.  **计算五个进程的总大小**:
>     *   总大小 = 5 * (单个页表大小) = 5 * 2 MiB = 10 MiB.

**【判断题】**

> 1.  In a system where multiple programs are running, the physical memory space must be larger than the total size of the virtual address spaces. (T/F) (2020-2021 P4)
>
> **答案**: F (False)
> **解析**: 虚拟内存的主要优点之一就是允许所有进程的虚拟地址空间总和远大于物理内存。

> 2.  Multiple levels of page tables can also be used to reduce the total amount of page table storage. (T/F) (2018-2019 P72, P80)
>
> **答案**: T (True)
> **解析**: 多级页表通过仅为已分配的虚拟地址区域创建次级页表来节省空间。如果一个大的地址段未使用，就不需要为它创建页表项。

> 3.  The starting address of the page table is stored in TLB. (T/F) (2018-2019 P72, P80)
>
> **答案**: F (False)
> **解析**: 页表的起始地址存储在CPU的一个专用寄存器中，即页表基址寄存器 (Page Table Base Register)。TLB存储的是具体的页表项 (PTE)，而不是整个页表的地址。

> 4.  The page table is stored in main memory. (T/F) (2021-2022 P97, P105, 2023-2024 P124)
>
> **答案**: T (True)
> **解析**: 页表本身作为一种数据结构，是存放在物理主存中的。

> 5.  Virtual memory allows a single program to expand its address space beyond the limits of main memory. (T/F) (2010-2011 P114, 2023-2024 P124)
>
> **答案**: T (True)
> **解析**: 这是虚拟内存的核心功能之一。

> 6. The page table is stored in the disk. (T/F) (2010-2011 P115)
>
> **答案**: F (False)
> **解析**: 页表必须存放在主存中，以便MMU能够快速访问它进行地址翻译。如果页表在磁盘上，每次地址翻译都需要磁盘I/O，系统将无法工作。
