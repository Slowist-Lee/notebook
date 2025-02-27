# 概统历年卷勘误(个人版)

!!! warning
    建议以mkdocs版为准！(因为在及时更新!)    
    最近发现当时做的错误有点多，可以先在评论区/issue内看看有没有说明的纠错~  
    主要slowist的概统已经忘的差不多了 TT 而且手上也没有卷子和具体的题目，再加上期末周太难顶了没时间研究概统，可能很难马上改正，如果发现有错的话，有如下两种方式：  
    1. 【推荐】直接在仓库内进行Pr（因为我也不太会改）   
    2. 【推荐】 如果我没把giscus玩坏，在评论区指出（最好附上正确答案（懒得敲公式也可以拍照）/在仓库内提issue   
    3. 以任何渠道（98、vx、邮箱、钉钉）私发我（但是我可能做的只有放到原文的评论区内）   

## 2022-2023 第一学期
### 填空 Ex.4 第二空

个人做下来感觉有一个正负号写反了

$Cov(aX-Y,X+Y)=Cov(aX,X+Y)-Cov(Y,X+Y)=aDx+aCov(X,Y)-Cov(X,Y)-DY$
$=a+(a-1)\sqrt{1\times4}\times \frac{1}{2}-4=2a-5=0$
$\Rightarrow a=\frac{5}{2}$

### 填空 Ex.4 第三空

可以算出$X-1$~$N(0,1) \Rightarrow (X-1)^2$~$\chi(1)$

同理，$(\frac{Y-X-1}{\sqrt 3})^2$~$\chi(1)$

$\Rightarrow F(1.1)$分布

### 填空 Ex.5 (3) 没有答案

> 这题我不太确定qwq 不太会

∵题干中 $H_1:\mu<2$, 所以判断是左边假设

∴计算检验统计量$\frac{\overline{X}-\mu}{\sigma / \sqrt{n}}=\frac{2.98-2}{2/ \sqrt{16}}=1.96$

$P-=1-\Phi (1.96)$


### 大题二、(2)

题干少了条件，设$F(X,Y)$ 为联合分布函数

> 我一开始甚至看成了F分布 手动ac01

### 大题三、(1)

最后答案算出来好像是 $\frac{5}{24}$

### 大题三、(3)

$F(m)$的最终结果里第二行第三行，z和m写反了，别抄错了 ac01

## 2021-2022 第一学期 

### 填空 Ex.2 第二空

标准差是24，打错了

### 大题三、(1)

==Point 1==

$Y^2$ ~ $E(\frac{1}{2})$ 没有证明，这里给出一个补充捏

设$Z=Y^2$ 所以 $F_Z(z)=P(Y≤z^2)=P(Y≤ \sqrt z)$

∵$Y$ ~$E(1)$ ∴ $F_Y(y)=1-e^{-y}$   即 $\Rightarrow$ $F_Z(z)=P(Y≤\sqrt z)=1-e^{-\frac{1}{2}z}$

所以$f_Z(z)=\frac{1}{2}ze^{-\frac{1}{2}z}$

对应指数分布的式子，$\lambda = \frac{1}{2}$

所以$E(Y^2)=\frac{1}{\lambda}=2$


==Point 2==

$DW^2=D(X^2Y^2)$  好像有问题

这里给出两种做法：

$DW=DXY=E(X^2Y^2)-E^2(XY)$

而 $E(X^2Y^2)=E(X^2)E(Y^2)=1\times 2 =2$

$E(XY)=E(X)E(Y)=0$

$E^2(XY)=0  ∴DW=2-0=2$

**法二**：

或者用一个~~我也不知道哪来的公式~~

$DW=DXY=DXDY+DX(EY)^2+DY(EX)^2=1\times 1+ 1\times 1 +0 =2$

### 大题四、(3)

个人算出来的结果是 ==是== 

计算过程如下：

$f_Y(y)=\int_{-1}^1 \frac{1}{2}(1-xy)dx=[\frac{1}{2}x-\frac{1}{4}x^2y]_{-1}^1=1$ $(0<y<1)$

上一问里我们应该算过$f_X(x)=\frac{1}{2}(1-\frac{x}{2})$

$\Rightarrow F_X(x)=\int_{-1}^x(\frac{1}{2}-\frac{1}{4}x)=-\frac{1}{8}x^2+\frac{1}{2}x+\frac{5}{8}$

$F_{|X|}(x)=P(|X|≤x)$

当$x>0$时，原式=$P(-x≤X≤x)=F_X(x)-F_X(-x)=x \Rightarrow f_{|X|}(x)=1$

下面来算$F_{|X|Y}(x,y)=P(|X|≤x,Y≤y)=\int_{-x}^{x}dx\int_0^y\frac{1}{2}(1-xy)dy=\int_{-x}^{x}(\frac{1}{2}y-\frac{1}{4}xy^2)dx=xy$

故$f_{|X|,Y}(x,y)=\frac{\partial^2F}{\partial x \partial y}=1$

故$f_{|X|}(x) \cdot f_{|Y|}(y)=f_{|X|,Y}(x,y)=1 \Rightarrow$ 独立

### 大题五、(2)(3)

#### 第二小题

这里不需要考虑第二类错误。因为要算第二类错误需要告知真实的$\mu$的大小，而题目里没有说。一般而言，数理统计里面没有明说第二类错误的话都是指第一类错误

检验统计量的值为$Z=\frac{\overline{X}-\mu}{\sigma/\sqrt{n}}=-2.5$

犯第一类错误即Z的值落在拒绝域内，即$-2.5<-Z_{\frac{\alpha}{2}}$，即$Z_{\frac{\alpha}{2}}>2.5$

$\Rightarrow \frac{\alpha}{2} = 1-\phi(2.5) \Rightarrow 犯错误的概率为0.0124$

#### 第三小题

与第二小题类似

检验统计量的值为$Z=\frac{\overline{X}-\mu}{\sigma/\sqrt{n}}=-0.625 * \sqrt{n}$

$\Rightarrow 1-\phi(0.625 * \sqrt{n}) = \frac{\alpha}{2} < \frac{0.05}{2} \Rightarrow 0.625 * \sqrt{n} > Z_{0.025} =1.96 \Rightarrow n \geq 10$

## 2021-2022 第二学期

### 填空 Ex.3 第二问没解析＆答案

个人给出的解析如下：

难点还是时间转换：$P(T>t)=P(N_t=0)$ 即在$t$天内未发生故障

∵$N_t$ 服从泊松分布 ∴$P(N_t=k) = e^{-\lambda}\frac{\lambda ^k}{k!}$

将$k=0$代入，$P(T>t)=P(N_t=0)=e^{-\lambda}=e^{-\frac{1}{72}t}$

故$P(T≤t)=1-e^{-\frac{1}{72}t}=F_T(t)$  $\Rightarrow$ $f(t)=\frac{1}{72}e^{-\frac{1}{72}t}$ $\Rightarrow  \lambda = \frac{1}{72}$

∴ T服从指数分布 $E(T)=\frac{1}{\lambda}=72$

### 大题三、(2)

>这题答案好像还是有点问题，我回头修一下，现在概统忘光了qwq    

答案显然从头错到尾，附上我做的答案

∵$P(Y=0)=\frac{2}{3} P(Y=1)=\frac{1}{3} ∴ P(M=0)=(\frac{2}{3})^5$

对于$Z_i=X_iY$ :

当$Y=0$, $Z_i=0$

当$Y=1$, $Z_i=X_i, X_i$~$E(1)$

设$F_{Z_i}(z)$是$z$的分布函数，$F_{Z_i}(z)=P(Z_i≤z)=P(Z_i=0)+P(Z_i≤1|Y=1)P(Y=1)=\frac{2}{3}+\frac{1}{3}(1-e^{-z}),z≥0$

所以$F_M(m)=P(M≤m)=P(max{Z_1,Z_2\dots Z_5}≤m)=(\frac{2}{3}+\frac{1}{3}(1-e^{-m}))^5$

综上，分布函数是：

$F_M(m) = \begin{cases} 0 & \text{if } m < 0 \\(\frac{2}{3}+\frac{1}{3}(1-e^{-m}))^5 & \text{if } m \geq 0 \end{cases}$

### 大题四、(1)

第一行、二行里指数漏了一个**负号**

即$f(x)=\frac{1}{\sqrt{2\pi}\sigma}exp\{-\frac{(x-\mu)^2}{2\sigma^2}\}$

### 大题六、(2)

我算出来卡方的结果好像是7.794……（仅供参考w)

最后一行, $\chi^2_{0.05}(2)=5.99$,所以结果应该是属于，拒绝原假设

## 2020-2021 第一学期

### 大题四、(1)

个人认为定义域有点问题：
$F(x,y)=0$ 对应的区间应该是$x>0$且$y<0$

### 大题六、(2)

会发现答案里的表格就有问题……$X≥4$的那一列，$(n\hat{p_i})$的理论频数3，≤5，不符合规则

所以应该把3、4、5、6都合并在一起

个人算出来的结果：

| X                   | 0   | 1    | 2    | ≥3   |
| ------------------- | --- | ---- | ---- | ---- |
| $(n_i)$频数           | 32  | 41   | 16   | 11   |
| $(p_i)$             | 0.3 | 0.36 | 0.22 | 0.12 |
| $(n\hat{p_i})$的理论频数 | 30  | 36   | 22   | 12   |

$\chi^2=\sum_{i=1}^4\frac{n_i^2}{np_i}-n≈2.547$  而 $\chi_{0.05}^2 = 5.99$

因此$H_0$成立

