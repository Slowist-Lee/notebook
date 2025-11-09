# 搜索
## 一、搜索问题模型
### 1. 搜索问题

搜索问题往往由以下部分组成：

- 状态空间（State Space）
- 每个状态下可以有的行动（actions）
- 转移模型 transition model
- 行为代价（cost）
- 开始状态（start state）
- 目标函数（goal test）

### 2. 状态的存储方式

- 状态图
- 搜索树

- Search Tree：
	- 搜索树的关键优势在于它**不需要预先存储所有的状态和转移**。相反，它从初始状态开始，**按需地生成和探索**可能到达的状态。当我们考虑一个当前状态时，我们只需要使用 `getNextState`, `getAction`, 和 `getActionCost` 方法来计算其子状态
	- **只存储当前正在探索的少量节点**，并迭代地用它们的子节点替换这些节点，从而克服了内存限制。这样，我们只需要在任何给定时间点维护搜索树的一小部分。
	- 每个状态/节点不仅编码状态本身，还编码状态空间图中从起始状态到给定状态的整个路径（可以直接输出而不需要再找一遍x）

## 二、无信息搜索 (Uninformed Search)

> [!NOTE] 适用条件
> 完全没有任何外界信息

（和最短路中的搜索非常的像）

一般的搜索过程：
1. 会维护一个外围边界（frontier），即目前正在探索的点（当前正在考虑的“岔路口”的列表），包含了一些我们已经探索了一部分但还没有到达终点的“部分路径”。
2. 从第$n \rightarrow n+1$的过程中：
	- 从这个“岔路口”列表中选择一个“岔路口”
	- 把它从我们的“岔路口”列表中移除
	- 考虑从这个“岔路口”出发的所有可能的下一步行动，生成新的“岔路口”（也就是它的**子节点**）
3. 直到我们找到目标状态

伪代码：(搬运自[here](https://kg.darstib.cn/note/cs188/note/02-State_Spaces_Uninformed_Search/#Uninformed-Search))

```python
function TREE-SEARCH(problem, frontier) return a solution or failure
    frontier ← INSERT(MAKE-NODE(INITIAL-STATE[problem]), frontier)
    while not IS-EMPTY(frontier) do
        node ← POP(frontier)
        if problem.IS-GOAL(node.STATE) then
            return node
        end
        for each child-node in EXPAND(problem, node) do
            add child-node to frontier
        end
    end
    return failure

function EXPAND(problem, node) yields nodes
    s← node.STATE
    for each action in problem.ACTIONS(s) do
        s′ ← problem.RESULT(s, action)
    end
    yield NODE(STATE=s′, PARENT=node, ACTION=action)
```

### 2.1 DFS - 深度优先搜索

- 边界表示（存储Frontier的数据结构）：栈
- 算法逻辑：移除最深的节点，并用它的子节点替换它在边界中的位置
- 完备性（Completeness, 即能否找到这个解）：否。如果状态空间图中存在**环路 (cycles)**，这必然意味着对应的搜索树可能会有**无限的深度**。
- 最优性 (Optimality) ：否。深度优先搜索仅仅找到搜索树中“最左边”的解决方案，**不考虑路径成本**，因此不是最优的。
- 时间复杂度：$O(b^m)$

### 2.2 BFS - 广度优先搜索

- 边界表示：队列
- 算法逻辑：总是从**起始节点**开始，选择当前**最浅**的**边界节点**进行**扩展**。类似层序遍历，遍历了这一整层都不符合条件再进行跳过。
- 完备性：是。如果一个解存在，那么最浅节点 s 的深度必然是有限的，所以 BFS 最终一定会搜索到这个深度。因此，它是完备的。
- 最优性：否。BFS 全程并没有考虑路径成本。特殊情况是所有边的成本都相等，则是最优的。
- 时间复杂度：$O(b^s)$。在最坏的情况下，我们必须搜索 $1+b+b^2+...+b^s$ 个节点
- 空间复杂度：$O(b^s)$。

### 2.3 UCS - 一致代价搜索 (Uniform Cost Search)

核心逻辑：真正关注到达每个状态的**总成本**

- 边界表示：Priority Queue（堆），值为从起始节点到 v 的**路径成本**
- **完备性 (Completeness)**：是。一致代价搜索是完备的。如果一个目标状态存在，它必然存在一条长度有限的最短路径。
- 最优性：是。由于我们按照路径成本递增的顺序探索节点，我们保证找到到达目标状态的最低成本路径。
- 时间复杂度：定义最优路径成本为 $C^∗$，状态空间图中任意两个节点之间的最小成本为 $ϵ$。那么，我们大致需要探索深度从 1 到 $C^∗/ϵ$ 的所有节点，导致运行时间为 $O(b^{{C^∗}/ϵ})$。

## 三、有信息搜索 (Informed Search)

特点：heuristics - 启发式

**下界 (Lower bound):** 我们通常希望我们的启发式函数估计的剩余距离**小于或等于**实际的剩余距离。这样的启发式函数被称为**可采纳的 (admissible) 启发式**。如果启发式函数是实际剩余距离的下界，那么 A\* 搜索在满足某些条件下可以保证找到最优解。

**松弛问题 (Relaxed problems):** 为了设计一个能够提供下界的启发式函数，一个常用的方法是考虑原问题的**松弛版本**。松弛问题是指我们去除了原问题的一些约束条件，使得问题更容易解决。解决这个更容易的松弛问题的最优解通常可以作为原问题剩余距离的一个可采纳的启发式估计。因为在约束更少的情况下找到的“最短路径”的长度，必然小于或等于在约束更多的情况下找到的实际最短路径的长度。

例如：

解决路径问题的一个常用启发式方法是曼哈顿距离，对于两个点 (x1​, y1​) 和 (x2​, y2​)，其定义如下：

$Manhattan(x_1​,y_1​,x_2​,y_2​)=∣x_1​−x_2​∣+∣y1_​−y2​∣$

启发式函数是帮助我们估计从当前状态到目标状态的"好坏程度"的工具。一个好的启发式函数能够引导搜索朝着更有希望的方向前进，从而提高搜索效率。为了保证 A\* 搜索的最优性，我们通常希望使用可采纳的启发式函数，即**可采纳的启发式函数估计的剩余成本永远不会高于实际的剩余成本**。一种常用的设计可采纳启发式函数的方法是解决原问题的**松弛版本**，并将松弛问题的最优解作为原问题的启发式估计。在吃豆人游戏中，曼哈顿距离就是一个简单而有效的可采纳的启发式函数，用于估计从当前位置到目标位置的剩余步数。

如图，没有墙壁，直接走的情况一般是步数的下界；


有了启发式，我们的智能体在决定执行哪个动作时，就能很容易地实现偏向于扩展那些估计离目标状态更近的状态的逻辑。

### 3.1 Greedy Search（贪婪搜索）

- 算法逻辑：选择边界中具有**最低启发式值**的节点进行扩展，这对应于它认为最接近目标的状态。
- 边界表示：贪婪搜索的操作方式与一致代价搜索 (UCS) 完全相同，都使用**优先队列 (priority queue)** 来表示 Frontier
- **不保证完备性:** 贪婪搜索可能会因为选择了不合适的路径而陷入无限循环，或者虽然存在目标状态，但它一直朝着错误的方向探索而错过了目标。
- **不是最优的:** 贪婪搜索只关注当前看起来最好的状态，而不考虑到达该状态的实际成本。因此，它找到的第一个目标状态的路径成本很可能不是最低的。
- **行为不可预测:** 贪婪搜索的性能很大程度上依赖于启发式函数的质量。如果启发式函数非常准确，贪婪搜索可能很快就能找到一个不错的解（但不保证最优）。但如果启发式函数很差，它可能会误导搜索朝着远离目标的方向前进，导致效率很低，甚至找不到解。它可能会像一个“短视”的 DFS，沿着一条看起来很有希望但最终是死胡同的路径一直探索下去。

### 3.2 A\*搜索算法

A\*搜索是UCS和Greedy Search的结合体，它定义了一个估计总成本 $f(n)=g(n)+h(n)$, 其中$n$是当前所在的节点，$g(n)$是已经付出的成本，$h(n)$是从$n$到目标函数的估计成本（下界）。

- **边界表示**：显然又是Priority Queue.
- **完备性:** 如果存在到达目标状态的路径，A\* 搜索最终一定会找到它。
- **最优性:** A\* 搜索找到的第一个目标状态的路径一定是成本最低的（最优解）。

#### 1. Admissibility - 可采纳性

从式子中我们发现，由于总成本$f(n)=g(n)+h(n)$，所以最终的算法实现还需要知道$h(n)$如何来取。在使用 A\* 树搜索时，保证最优性的条件被称为可采纳性 (admissibility)。可采纳性约束规定，一个可采纳的启发式函数估计的值既不是负数也不是高估。

将 $h^*(n)$ 定义为从给定节点 $n$ 到达目标状态的真实最优前向成本，我们可以用数学方式表示可采纳性约束如下:

$\forall n,0≤h(n)≤h^*(n).$

| **特征**   | **$h(n)$ (启发式函数)**                                       | **$h^∗(n)$ (最优启发式函数)**  |
| -------- | -------------------------------------------------------- | ----------------------- |
| **本质**   | **估计值**                                                  | **真实值**                 |
| **获取方式** | 通过设计启发式函数得到 (Designed)                                   | 通常在搜索过程中**未知**          |
| **准确性**  | 可能低估、准确估计，但不能高估                                          | 完全准确                    |
| **用途**   | 用于指导 A\* 搜索的优先级，帮助算法更有效地找到解 (Guides A\* search priority) | 由于未知，只是推导过程里的上界，并不能直接使用 |

下面证明：对于给定的搜索问题，如果启发式函数 h 满足可采纳性约束(admissibility constraint)，那么在该搜索问题上使用带有 $h$ 的 A\* 树搜索将产生一个最优解。

Proof:

假设在给定搜索问题的搜索树中存在两个可达的目标状态：一个最优目标 A 和一个次优目标 B。由于 A 可以从起始状态到达，因此 A 的某个祖先节点 n（包括 A 本身）当前必须在边界上。下证 $n$ 将在 B 前被 expand:

1. $g(A)<g(B)$。 因为 A 被认为是最优的，而 B 是次优的，所以我们可以得出结论，A 到起始状态的后向成本比 B 到起始状态的后向成本要低。
2. $h(A)=h(B)=0$。 因为我们假设我们的启发式函数满足可采纳性约束。由于 A 和 B 都是目标状态，从 A 或 B 到目标状态的真实最优成本 $h^∗(n)$ 都是 0；$\therefore 0≤h(n)≤0$。

由上述，又$\because \forall k \in I, f(k)=h(k)+g(k) \Rightarrow$
$f(A)=g(A)+h(A)=g(A)<g(B)=g(B)+h(B)=f(B)$

3. $f(n)\leq f(A).$ 通过 $h$ 的可采纳性，$f(n)=g(n)+h(n)≤g(n)+h^∗(n)=g(A)=f(A)$。由于 $n$ 在最优路径上，通过节点 $n$ 的总成本最多是 A 的真实后向成本，这也是 A 的总成本。

综合上面的不等式，有
$\therefore f(n) \leq f(A) <f(B)$， 因此Expand顺序是 $n\rightarrow A \rightarrow B$

∴所有 A 的parent node（包括 A 本身）都在 B 之前被 Expand.

#### 2. 一个小bug

如图所示的状态转换图，C作为次优解将难以被访问。

<!-- ![](image/Pasted%20image%2020250509171218.png) -->

因此，为了在 A\* 图搜索中保持最优性，我们需要在重新访问一个状态时，检查是否找到了一条到达该状态的更低成本的路径。如果是，我们需要更新该状态的成本，并将其重新放入边界（优先队列）中，以便从新的更低成本路径继续搜索。

```python
function A*-GRAPH-SEARCH(problem, frontier) return a solution or failure
    reached ← an empty dict mapping nodes to the cost to each one #记录是否被访问过
    frontier ← INSERT((MAKE-NODE(INITIAL-STATE[problem]),0), frontier) #初态
    while not IS-EMPTY(frontier) do
        node, node.CostToNode ← POP(frontier) #边界条件中最小的cost
        if problem.IS-GOAL(node.STATE) then 
	        return node #达到目标状态，结束程序
	    end
        if node.STATE is not in reached or reached[node.STATE] > node.CostToNode then #如果没被访问过，或者当前的解比之前更优
            reached[node.STATE] = node.CostToNode #标注为已访问
            for each child-node in EXPAND(problem, node) do
                frontier ← INSERT((child-node, child-node.COST + CostToNode), frontier) #expand这个节点
            end
    return failure
```

#### 3. 支配性（Dominance）

如果启发式函数 $h_a$​ 支配启发式函数 $h_b$​，那么对于状态空间图中的每个节点，$h_a$​ 估计的目标距离大于或等于 $h_b$​ 估计的目标距离。数学上，

$\forall n:h_a​(n)≥h_b​(n)$

支配性非常直观地捕捉了一个启发式函数比另一个更好的概念 - 如果一个可采纳的启发式函数支配另一个，它必然更好，因为它总是更接近地估计从任何给定状态到目标的距离 （由于约束$h_a(n)\leq h_a^*(n)$）.

特例：**平凡启发式 (trivial heuristic)** 定义为 $h(n)=0$，使用它会将 A* 搜索简化为 UCS。

## 四、Local Search 局部搜索算法

Local Search解决的问题和之前有一点偏差，他不要求返回Path, 但需要找到目标状态，即：Local search algorithms allow us to find goal states without worrying about the path to get there： 找目标状态，不在意到达的路径。
### 4.1 爬山搜索

爬山搜索算法，也称为最速上升法，是一种局部搜索算法。它的基本思想是从当前所处的状态开始，考察其所有相邻的状态。在这些相邻状态中，算法会选择那个能够使目标函数值增加最多的状态，并移动到该状态。这个过程会不断重复，直到无法找到比当前状态更好的相邻状态为止。

爬山搜索算法不维护一个完整的搜索树。它只需要记住当前的状态以及该状态下目标函数的值。这意味着爬山搜索算法的内存开销通常比较小。

伪代码:

### 4.2 模拟退火搜索

- 结合随机游走（在邻近状态中随机移动）和爬山搜索
- 在模拟退火的每个时间步，算法会随机选择一个邻近状态。如果这个邻近状态的目标函数值更高，那么这个移动会被无条件接受。如果目标函数值更低，那么这个移动会以一定的概率被接受。这个接受的概率由一个称为“温度”（temperature）的参数决定。初始时，温度很高，这意味着算法更容易接受“坏”的移动（目标函数值下降的移动），从而有助于跳出局部最优解。随着时间的推移，温度会按照一定的“降温策略”（cooling schedule）逐渐降低，这使得算法越来越不容易接受“坏”的移动，从而逐渐收敛到最优解。

 理论上能够证明，如果温度下降的速度足够缓慢，模拟退火算法找到全局最优解的概率会趋近于1，这意味着它在理论上是完备的。

### 4.3 局部束搜索

 局部束搜索（local beam search）是爬山搜索的另一种变体。与标准爬山搜索每次只维护一个当前状态不同，局部束搜索在每次迭代中维护 k 个状态（可以想象成 k 条并行的搜索“线程”）。

 算法首先随机生成 k 个初始状态。在每次迭代中，对于当前的 k 个状态，算法会生成它们所有的邻居状态。然后，从所有这些邻居状态中选择最好的 k 个状态作为下一次迭代的当前状态。

局部束搜索不是简单地运行 k 个独立的爬山搜索。关键在于，它会考虑所有 k 个当前状态的所有邻居状态，并从中选出全局最好的 k 个作为下一步的状态。这意味着不同的“线程”之间可以竞争和协作。如果在搜索过程中，任何一个“线程”找到了最优解，算法就会停止。

 由于每次都选择全局最好的 k 个后继状态，那些目标函数值较高的“好”线程产生的后继状态更有可能被选中，这实际上引导着其他的线程也向着这些有希望的区域移动，从而实现了某种程度的信息共享。

类似于标准的爬山搜索，局部束搜索也容易陷入平坦区域。为了解决这个问题，人们提出了随机束搜索（stochastic beam search），它与随机爬山搜索类似，在选择下一个 k 个状态时引入一定的随机性，允许选择一些不是局部最优的邻居状态，从而有助于跳出平坦区域。

#### 4.4 遗传算法

算法流程：
- 初始化 k 个随机状态，这些状态在遗传算法中被称为“种群”（population），每个状态被称为“个体”（individual）。每个个体通常被表示为一个有限字母表上的字符串，这个字符串可以看作是问题解的一种编码方式。

可以看图：（八皇后问题）

- 定义适应度/评估函数：越接近想要的结果，这个值就越高。比如八皇后问题，一个常用的适应度函数是棋盘上不互相攻击的皇后对的数量。
- 选择“繁殖”的个体的概率与它们的适应度值成正比，适应度越高的个体越有可能被选中作为“父母”（parents）
- 通过“交叉”（crossover）操作产生“后代”（offspring）：将两个父代个体的部分字符串进行交换
- 每个后代都有一定的独立概率发生“变异”（mutation），即随机改变其字符串中的某个或某些字符

伪代码：

```python
function genetic-algorithm(population, Fitness-Fn) returns an individual
	'''
	inputs: population: sets of individuals, 不同的解
	Fitness-Fn: 适应度函数
	'''
	repeat
		new population ← empty set
		for i=1 to size(population) do
			x ← random-selection(population, Fitness-Fn)
			y ← random-selection(population, Fitness-Fn) 
			# 利用Fitness-Fn函数，在population里面以一定概率找到父母
			child ← reproduce(x,y) # 基于x,y繁衍
			if(small random probablitity) then 
				child ← mutate(child) #小概率变异
			end
			add child to new_population
		end
		population ← new_population
		until some individuals i fit enough, or enough time
		return the best individual in population, according to finess0fn
function REPRODUCE(x, y) returns an individual
	'''
	inputs: x, y, parent individuals
	'''
	n ← LENGTH(x)
	c ← random number from 1 to n
return APPEND(SUBSTRING(x, 1, c), SUBSTRING(y, c + 1, n))
```

 类似于随机束搜索，遗传算法也试图在搜索空间中向着更好的解移动，并且通过种群中的多个个体来探索不同的区域，并进行信息交换（通过交叉）。遗传算法的主要优势在于交叉操作。通过交叉，那些在进化过程中形成的、能够带来较高适应度值的“基因块”（字符串片段）可以与其他类似的优秀基因块组合，从而有可能产生具有更高总适应度值的解决方案。这使得遗传算法在解决复杂优化问题时具有强大的能力。

