# Tools

!!! abstract
	PKU-HPC 2nd. Lec1 赛前培训. - Tools

!!! warning ""
	此笔记位于摸鱼初期

>03年开启的多核时代。因为单核性能非常高了，再提升非常困难。想利用好CPU的多核资源，就需要mpi的进程管理，openmp/Pthread的线程管理以及混合并行。GPU是和CPU的异构硬件，需要一套另外的操作


DLP: data level parallelism

SIMD: 以向量的形式同时处理多组数据
我们要做的：自动向量化或者显式使用向量化的指令

线程模型 pthread / OpenMP 要求分给多个核心 【都有相应课程/教材】

OpenMP

```c
#pragma omp parallel for //指导编译器用多线程编译
for(int i=0; i<N;i++){
	result[i]=f(data[i]);
}
```

异构计算：

GPU/NPU 只需要 SIMT - GPU 的 课程



多行并行：通过高速并行线路，组成集群




![](image/Pasted%20image%2020250113194013.png)
链接： SSH windows terminal

![](image/Pasted%20image%2020250113194311.png)
-p: 可以指定对应的端口 -i 指定公钥

可以编辑 `~/.ssh/config` 
下次就可以`ssh network`
尽量不要密码登录：

![](image/Pasted%20image%2020250113194440.png)

传输文件：

![](image/Pasted%20image%2020250113194505.png)

`ls -lah` 文件/大小/修改时间

![](image/Pasted%20image%2020250113195906.png)
linux里用`echo $PATH`来找到环境变量

链接还有一些用法是一些程序在编译的时候会用到的库是写死的名称。可以用链接的方式给出这个库。比如libcuda.so/libcuda.so.1，其实可能链接到的是同一个库

![](image/Pasted%20image%2020250113200328.png)

gcc/g++ compiler driver

Make: 写好规则

语言：Makefile
本质：命令执行器

注意：每个命令前必须是Tab

例：最基本的用法

```makefile
program: main.o utils.o //这是依赖
	gcc -o program main.o utils.o
Main.o: main.c
	gcc -o main.o main.c
```

可以先调一下变量
![](image/Pasted%20image%2020250113200935.png)

伪目标：
![](image/Pasted%20image%2020250113200953.png)

一般不会用到：

![](image/Pasted%20image%2020250113201030.png)

`git clone ... --depth=1`

![](image/Pasted%20image%2020250113201911.png)
编译openmpi的例子↑

CMAKE: 优雅的Builder
可以用cmake,make,ninja
CMakeLists.txt

![](image/Pasted%20image%2020250113202400.png)

>编译环节最痛苦的是这个大东西本身依赖的库可能有版本问题，或者不能按他给出的安装脚本一键安装。不出任何问题的话从应用的角度来说cmake就是在通过CMakeLists.txt。cd build之后cmake ..再make和make install。make本身是需要一个Makefile

![](image/Pasted%20image%2020250113203005.png)
Python:
conda的miniforge前端

![](image/Pasted%20image%2020250113203253.png)
