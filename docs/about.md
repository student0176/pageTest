  DFT叫做离散版本的Fourier变换，在信号处理方面发挥着重要作用。初次接触只感觉到时域频域绕来绕去，公式异常繁复。如果背会公式的话，倒是可以慢慢玩味它背后的思想。本文就是我综合了很多人的真知灼见（当然也踩了一些坑）后，玩味的结果，目的是对一个想尝试理解这些内容的读者，帮他们缩短一些找资料的时间，也希望能够在不扯太多新名词的前提下把话说清楚。

### 写在前面
  * DFT就是找出序列在一组特定基底下的系数，这组基底当然是经过了巧妙地设计的，它的每一列都表示一个固定角频率的绕单位圆运动的采样点，不同的列对应不同倍频。求出系数后，原来的序列当然也就表达成了好几列的线性组合，输入的采样序列就分解为不同频率的采样序列的叠加；
  * 数学工具主要用到分块矩阵、复数的基本性质、简单的求极限、等比数列求和等；
  * 任何问题都有多种看待方式，也必须从各个角度去尝试理解，因为这样会感到快乐，从而形成良好的正反馈，本文就是在这种快乐状态中产生的；
  * 懒惰的人不会这样做，浮躁的人认为没必要这样做，所以他们的快乐较少，快乐少又会加深懒惰与浮躁，形成恶性的正反馈，希望吾侪引以为戒，苟日新日日新又日新。

### 准备工作    
* 从一个**线性代数**问题出发：求解向量$\beta$在DFT基底下的系数$X$
   
\[\beta  = \left( {\begin{array}{*{20}{c}} {{e^{\frac{{2\pi i}}{{\rm{4}}}{\rm{ \times 0 \times 0}}}}}&{{e^{\frac{{2\pi i}}{{\rm{4}}}{\rm{ \times 0 \times 1}}}}}&{{e^{\frac{{2\pi i}}{{\rm{4}}}{\rm{ \times 0 \times 2}}}}}&{{e^{\frac{{2\pi i}}{{\rm{4}}}{\rm{ \times 0 \times 3}}}}}\\ {{e^{\frac{{2\pi i}}{{\rm{4}}}{\rm{ \times 1 \times 0}}}}}&{{e^{\frac{{2\pi i}}{{\rm{4}}}{\rm{ \times 1 \times 1}}}}}&{{e^{\frac{{2\pi i}}{{\rm{4}}}{\rm{ \times 1 \times 2}}}}}&{{e^{\frac{{2\pi i}}{{\rm{4}}}{\rm{ \times 1 \times 3}}}}}\\ {{e^{\frac{{2\pi i}}{{\rm{4}}}{\rm{ \times 2 \times 0}}}}}&{{e^{\frac{{2\pi i}}{{\rm{4}}}{\rm{ \times 2 \times 1}}}}}&{{e^{\frac{{2\pi i}}{{\rm{4}}}{\rm{ \times 2 \times 2}}}}}&{{e^{\frac{{2\pi i}}{{\rm{4}}}{\rm{ \times 2 \times 3}}}}}\\ {{e^{\frac{{2\pi i}}{{\rm{4}}}{\rm{ \times 3 \times 0}}}}}&{{e^{\frac{{2\pi i}}{{\rm{4}}}{\rm{ \times 3 \times 1}}}}}&{{e^{\frac{{2\pi i}}{{\rm{4}}}{\rm{ \times 3 \times 2}}}}}&{{e^{\frac{{2\pi i}}{{\rm{4}}}{\rm{ \times 3 \times 3}}}}} \end{array}} \right)\left( {\begin{array}{*{20}{c}} {{x_0}}\\ {{x_1}}\\ {{x_2}}\\ {{x_3}} \end{array}} \right){\rm{ = }}\left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}\\ {\rm{1}}&\omega &{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{3}}}}\\ {\rm{1}}&{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{6}}}}\\ {\rm{1}}&{{\omega ^{\rm{3}}}}&{{\omega ^{\rm{6}}}}&{{\omega ^{\rm{9}}}} \end{array}} \right)\left( {\begin{array}{*{20}{c}} {{x_0}}\\ {{x_1}}\\ {{x_2}}\\ {{x_3}} \end{array}} \right)  {\rm{ = }}\left( {\begin{array}{*{20}{c}} {{\alpha _0}}&{{\alpha _1}}&{{\alpha _2}}&{{\alpha _3}} \end{array}} \right)X\]

若$n$次单位根$e^{\frac{2\pi i}{n}}=\omega$，由等比数列求和有

\[\sum\limits_{j = 0}^{n - 1} {{\omega ^{lj}}} {\omega ^{kj}} = \frac{{1 - {\omega ^{(l + k)n}}}}{{1 - {\omega ^{l + k}}}} = \left\{ {\begin{array}{*{20}{c}} n&{(l + k)\bmod n = 0}\\ 0&{(l + k)\bmod n \ne 0} \end{array}} \right.\]

对${\alpha _j}{\rm{ = }}\left( {\begin{array}{*{20}{c}} {{\omega ^{0j}}}\\ {{\omega ^{1j}}}\\  \vdots \\ {{\omega ^{(n - 1)j}}} \end{array}} \right)$，其分量满足${\alpha _j}[p] = {\omega ^{jp}} = \overline {{\omega ^{ - jp}}}  = \overline {{\omega ^{jn - jp}}}  = \overline {{\alpha _j}[n - p]}$ ,$j=0,1,...,n-1$
，这个叫**共轭对称性**，则

\[\left( {\begin{array}{*{20}{c}} {{x_0}}\\ {{x_1}}\\ {{x_2}}\\ {{x_3}} \end{array}} \right){\rm{ = inv}}\left( {\begin{array}{*{20}{c}} 1&1&1&1\\ 1&\omega &{{\omega ^2}}&{{\omega ^3}}\\ 1&{{\omega ^2}}&{{\omega ^4}}&{{\omega ^6}}\\ 1&{{\omega ^3}}&{{\omega ^6}}&{{\omega ^9}} \end{array}} \right)\beta {\rm{ = }}\frac{1}{4}\left( {\begin{array}{*{20}{c}} 1&1&1&1\\ 1&{{\omega ^{ - 1}}}&{{\omega ^{ - 2}}}&{{\omega ^{ - 3}}}\\ 1&{{\omega ^{ - 2}}}&{{\omega ^{ - 4}}}&{{\omega ^{ - 6}}}\\ 1&{{\omega ^{ - 3}}}&{{\omega ^{ - 6}}}&{{\omega ^{ - 9}}} \end{array}} \right)\beta  = \frac{1}{4}\left( {\begin{array}{*{20}{c}} {{{\bar \alpha }_0}}&{{{\bar \alpha }_1}}&{{{\bar \alpha }_2}}&{{{\bar \alpha }_3}} \end{array}} \right)\beta  = \frac{1}{4}\sum\limits_{j = 0}^3 {{{\bar \alpha }_j}{\beta _j}} \]

哦不对...应该用下面这种分块... 

\[\left( {\begin{array}{*{20}{c}} {{x_0}}\\ {{x_1}}\\ {{x_2}}\\ {{x_3}} \end{array}} \right){\rm{ = inv}}\left( {\begin{array}{*{20}{c}} 1&1&1&1\\ 1&\omega &{{\omega ^2}}&{{\omega ^3}}\\ 1&{{\omega ^2}}&{{\omega ^4}}&{{\omega ^6}}\\ 1&{{\omega ^3}}&{{\omega ^6}}&{{\omega ^9}} \end{array}} \right)\beta  = \frac{1}{4}\left( {\begin{array}{*{20}{c}} {{\alpha _0}^H}\\ {{\alpha _1}^H}\\ {{\alpha _2}^H}\\ {{\alpha _3}^H} \end{array}} \right)\beta  = \frac{1}{4}\left( {\begin{array}{*{20}{c}} {{\alpha _0}^H\beta }\\ {{\alpha _1}^H\beta }\\ {{\alpha _2}^H\beta }\\ {{\alpha _3}^H\beta } \end{array}} \right)\]

其中${\alpha ^H} = {{\bar \alpha }^T} = \overline {{\alpha ^T}}$，将$X$代回得到恒等式

\[\beta  =  \frac{1}{{\rm{4}}}({\alpha _0}^H\beta ){\alpha _0} +\frac{1}{{\rm{4}}}({\alpha _1}^H\beta ){\alpha _1} + \frac{1}{{\rm{4}}}({\alpha _2}^H\beta ){\alpha _2} + \frac{1}{{\rm{4}}}({\alpha _3}^H\beta ){\alpha _3} = \sum\limits_{i = 0}^3 {\frac{{{\alpha _i}^H\beta }}{{{\alpha _i}^H{\alpha _i}}}} {\alpha _i}\]

* **我为何选择4阶的矩阵**

    首先如果为了省事，应该从低阶到高阶，所以应该从2阶阵出发，BUT很遗憾，${F_2} = \left( {\begin{array}{*{20}{c}} 1&1\\ 1&{ - 1} \end{array}} \right)$
 ，没有出现复单位根，不具备很强的说服力，所以选4阶。那为何不再看看8阶呢？这么说吧，且不论8阶矩阵的复数乘法，只是试着在64个格子内都填入特定的数字，没有人会觉得不枯燥，如果你真的这么尝试了，那么在看到后面的FFT算法后自然会更有感触。另外一个原因是，4阶的明白了后，自然可以充满自信地说 
$4 \to N$时显然成立！（这真的很显然）；所以从4阶阵入手，不仅方便举例，还不失一般性，还方便我写入，简直一石三鸟啊有木有！

### DFT
为何教科书上求DFT时候，在$X[k] = \sum\limits_{n = 0}^{N - 1} {{x_n}{W_N}^{nk}}$中将${W_N}^{nk} = {e^{ - \frac{{2\pi i}}{N}nk}}$定义为负幂次？我们当然可以说因为类比连续时候的$\int\limits_{ - l}^l {x(t){e^{ - i\frac{{n\pi t}}{l}}}} {\rm{d}}t$就是负的幂次，但换一种角度，因为我们最开始是想用那些正幂次来充当基底的向量，所以与
$\beta$做内积来求系数的任务自然就落到它们的共轭转置的头上了。

至于那个不知所措的$\frac{1}{4}$,其实放在DFT还是IDFT中都不要紧，为什么？因为对一个已知序列$f$，必然有

\[f = {I_4}f = \frac{1}{{\rm{4}}}\left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}\\ {\rm{1}}&\omega &{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{3}}}}\\ {\rm{1}}&{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{6}}}}\\ {\rm{1}}&{{\omega ^{\rm{3}}}}&{{\omega ^{\rm{6}}}}&{{\omega ^{\rm{9}}}} \end{array}} \right)\overline {\left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}\\ {\rm{1}}&\omega &{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{3}}}}\\ {\rm{1}}&{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{6}}}}\\ {\rm{1}}&{{\omega ^{\rm{3}}}}&{{\omega ^{\rm{6}}}}&{{\omega ^{\rm{9}}}} \end{array}} \right)} f\]

所以$\frac{1}{4}$想要放在前面后面还是中间，随它吧，有何干系？

至此，不妨再来体会一下教科书中那套广为人所诟病的通用流程：

* **STEP1** 先求下面这个东西，定义为DFT

\[F = \overline {\left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}\\ {\rm{1}}&\omega &{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{3}}}}\\ {\rm{1}}&{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{6}}}}\\ {\rm{1}}&{{\omega ^{\rm{3}}}}&{{\omega ^{\rm{6}}}}&{{\omega ^{\rm{9}}}} \end{array}} \right)} f\]

* **STEP2** 紧接着再求这个，定义为IDFT

\[f = \frac{1}{{\rm{4}}}\left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}\\ {\rm{1}}&\omega &{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{3}}}}\\ {\rm{1}}&{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{6}}}}\\ {\rm{1}}&{{\omega ^{\rm{3}}}}&{{\omega ^{\rm{6}}}}&{{\omega ^{\rm{9}}}} \end{array}} \right)F\]

这就是离散形式的Fourier变换了，事情还没有完！我们将目光着眼于关于$N$（偶数）的DFT 的矩阵(单位根$\omega=e^{i\frac{2\pi}{N}}$）

先算两个性质：首先$F_i = \alpha _i^Hf = \alpha _i^H\overline f  = \alpha _{N - i}^T\overline f  = \overline {F_{N-i}}$，取$i=\frac{N}{2}$ ，有${F_{\frac{N}{2}}} = \overline {{F_{\frac{N}{2}}}}$

其次注意到$a_i$与$F$都是复的列向量，都有这种**共轭对称性**，加上$\alpha_i^TF=Nf_i$
 是实的，这就仿佛是在告诉我们说：嗨！小伙子，只要你把我写成求和形式后化简，就能得到你想要的。何乐而不为呢？设 $F_j=m_je^{i\theta_j}$
 ,则 

\[{f_k} = \frac{1}{N}{\alpha _k}^TF = \frac{1}{N}\left( {\begin{array}{*{20}{c}} 1&{{e^{i\frac{{2\pi }}{N}k}}}& \ldots &{{e^{i\frac{{2\pi }}{N}\frac{N}{2}k}}}&{{e^{ - i\frac{{2\pi }}{N}(\frac{N}{2} - 1)k}}}& \ldots &{{e^{ - i\frac{{2\pi }}{N}k}}} \end{array}} \right)\left( {\begin{array}{*{20}{c}} {{F_0}}\\ {{F_1}}\\  \vdots \\ {{F_{\frac{N}{2}}}}\\ {\overline {{F_{\frac{N}{2} - 1}}} }\\  \vdots \\ {\overline {{F_1}} } \end{array}} \right){\rm{ = }}\frac{1}{N}(\sum\limits_{j = 1}^{\frac{N}{2} - 1} {2{\mathop{\rm Re}\nolimits} ({e^{i\frac{{2\pi }}{N}kj}}} {F_j}) + {F_0} - {F_{\frac{N}{2}}}) = \frac{1}{N}(\sum\limits_{j = 1}^{\frac{N}{2} - 1} {2{m_j}\cos( \frac{{2\pi }}{N}kj + {\theta _j}} ) + {F_0} - {F_{\frac{N}{2}}})\]

所以信号$f$就是对一组频率为$\frac{1}{N}$之倍数的信号采样后所得，假设被采样的信号是${\sin (2\pi \eta t + \phi )}$，每隔 $T_s$ 采样一次，采出 $N$ 个点，就有 $f_n={\sin (2\pi \eta (n{T_s}) + \phi )}$
，此时对应的频率为 $\eta T_s$ 。由于是同一个信号，取上上个式子 $n=L$ ，有 $\eta T_s=\frac{j}{N}$ ，即$\eta L=j$ ，这样就建立了 **连续信号的频率** & **时间长度**与 **$N$之index**的对应关系。


### FFT
*我偏不用蝶形图，你奈我何？*

还是从**4阶矩阵**出发（因为三维生物只能仰望四维）

我们拿到一个序列$f$ 后，现在**自信地**对其套用DFT公式

\[F = \overline {\left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}\\ {\rm{1}}&\omega &{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{3}}}}\\ {\rm{1}}&{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{6}}}}\\ {\rm{1}}&{{\omega ^{\rm{3}}}}&{{\omega ^{\rm{6}}}}&{{\omega ^{\rm{9}}}} \end{array}} \right)} f = \overline {\left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}\\ {\rm{1}}&\omega &{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{3}}}}\\ {\rm{1}}&{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{6}}}}\\ {\rm{1}}&{{\omega ^{\rm{3}}}}&{{\omega ^{\rm{6}}}}&{{\omega ^{\rm{9}}}} \end{array}} \right)} \left( {\begin{array}{*{20}{c}} {{f_0}}\\ {{f_1}}\\ {{f_2}}\\ {{f_3}} \end{array}} \right)\]

要是手算，需要16次复数的乘法，$N$阶序列需要$N^2$次复数乘法。FFT的提出者**Cooley&Tukey**说：我们为何不少算几次呢？因为这个矩阵**显然**可以进行如下的分解啊：

\[\left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}\\ {\rm{1}}&\omega &{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{3}}}}\\ {\rm{1}}&{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{6}}}}\\ {\rm{1}}&{{\omega ^{\rm{3}}}}&{{\omega ^{\rm{6}}}}&{{\omega ^{\rm{9}}}} \end{array}} \right) = \left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}\\ {\rm{1}}&\omega &{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{3}}}}\\ {\rm{1}}&{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{6}}}}\\ {\rm{1}}&{{\omega ^{\rm{3}}}}&{{\omega ^{\rm{6}}}}&{{\omega ^{\rm{9}}}} \end{array}} \right){I_4} = \left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}\\ {\rm{1}}&\omega &{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{3}}}}\\ {\rm{1}}&{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{6}}}}\\ {\rm{1}}&{{\omega ^{\rm{3}}}}&{{\omega ^{\rm{6}}}}&{{\omega ^{\rm{9}}}} \end{array}} \right){\left( {\begin{array}{*{20}{c}} {\rm{1}}&0&0&0\\ 0&0&1&0\\ 0&1&0&0\\ 0&0&0&1 \end{array}} \right)^2}\]

注意到

\[\left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}\\ {\rm{1}}&\omega &{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{3}}}}\\ {\rm{1}}&{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{6}}}}\\ {\rm{1}}&{{\omega ^{\rm{3}}}}&{{\omega ^{\rm{6}}}}&{{\omega ^{\rm{9}}}} \end{array}} \right)\left( {\begin{array}{*{20}{c}} {\rm{1}}&0&0&0\\ 0&0&1&0\\ 0&1&0&0\\ 0&0&0&1 \end{array}} \right){\rm{ = }}\left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}\\ {\rm{1}}&{{\omega ^{\rm{2}}}}&\omega &{{\omega ^{\rm{3}}}}\\ {\rm{1}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{6}}}}\\ {\rm{1}}&{{\omega ^{\rm{6}}}}&{{\omega ^{\rm{3}}}}&{{\omega ^{\rm{9}}}} \end{array}} \right){\rm{ = }}\left( {\begin{array}{*{20}{c}} {\rm{1}}&0&{\rm{1}}&0\\ 0&{\rm{1}}&{\rm{0}}&\omega \\ {\rm{1}}&{\rm{0}}&{{\rm{ - 1}}}&0\\ 0&{\rm{1}}&0&{{\rm{ - }}\omega } \end{array}} \right)\left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{1}}&{\rm{0}}&0\\ {\rm{1}}&{{\omega ^{\rm{2}}}}&{\rm{0}}&{\rm{0}}\\ {\rm{0}}&{\rm{0}}&{\rm{1}}&{\rm{1}}\\ 0&{\rm{0}}&{\rm{1}}&{{\omega ^{\rm{2}}}} \end{array}} \right){\rm{ = }}\left( {\begin{array}{*{20}{c}} {{I_2}}&{{D_2}}\\ {{I_2}}&{{\rm{ - }}{D_2}} \end{array}} \right)\left( {\begin{array}{*{20}{c}} {{F_2}}&0\\ 0&{{F_2}} \end{array}} \right)\]

最终得到

\[{F_4} = \left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}\\ {\rm{1}}&\omega &{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{3}}}}\\ {\rm{1}}&{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{6}}}}\\ {\rm{1}}&{{\omega ^{\rm{3}}}}&{{\omega ^{\rm{6}}}}&{{\omega ^{\rm{9}}}} \end{array}} \right){\rm{ = }}\left( {\begin{array}{*{20}{c}} {{I_2}}&{{D_2}}\\ {{I_2}}&{{\rm{ - }}{D_2}} \end{array}} \right)\left( {\begin{array}{*{20}{c}} {{F_2}}&0\\ 0&{{F_2}} \end{array}} \right)\left( {\begin{array}{*{20}{c}} {\rm{1}}&0&0&0\\ 0&0&1&0\\ 0&1&0&0\\ 0&0&0&1 \end{array}} \right)\]

将其作用到序列$f$上，最右边的矩阵只起到变换顺序的作用，不贡献乘法；中间的${F_{\rm{2}}}{\rm{ = }}\left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{1}}\\ {\rm{1}}&{{\rm{ - 1}}} \end{array}} \right)$
我们（事后诸葛亮）认为算1次复数乘法，有$2$个；左边的对角 $D$矩阵需要$2$ 次，共计 $O(F_4)=4=\frac{4}{2}\log4$
 次。都说到这儿了，不妨再看看$F_8$吧

\[{F_{\rm{8}}} = \left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}\\ {\rm{1}}&\omega &{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{3}}}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{5}}}}&{{\omega ^{\rm{6}}}}&{{\omega ^{\rm{7}}}}\\ {\rm{1}}&{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{6}}}}&{{\omega ^{\rm{8}}}}&{{\omega ^{{\rm{10}}}}}&{{\omega ^{{\rm{12}}}}}&{{\omega ^{{\rm{14}}}}}\\ {\rm{1}}&{{\omega ^{\rm{3}}}}&{{\omega ^{\rm{6}}}}&{{\omega ^{\rm{9}}}}&{{\omega ^{{\rm{12}}}}}&{{\omega ^{{\rm{15}}}}}&{{\omega ^{{\rm{18}}}}}&{{\omega ^{{\rm{21}}}}}\\ {\rm{1}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{8}}}}&{{\omega ^{{\rm{12}}}}}&{{\omega ^{{\rm{16}}}}}&{{\omega ^{{\rm{20}}}}}&{{\omega ^{{\rm{24}}}}}&{{\omega ^{{\rm{28}}}}}\\ {\rm{1}}&{{\omega ^{\rm{5}}}}&{{\omega ^{{\rm{10}}}}}&{{\omega ^{{\rm{15}}}}}&{{\omega ^{{\rm{20}}}}}&{{\omega ^{{\rm{25}}}}}&{{\omega ^{{\rm{30}}}}}&{{\omega ^{{\rm{35}}}}}\\ {\rm{1}}&{{\omega ^{\rm{6}}}}&{{\omega ^{{\rm{12}}}}}&{{\omega ^{{\rm{18}}}}}&{{\omega ^{{\rm{24}}}}}&{{\omega ^{{\rm{30}}}}}&{{\omega ^{{\rm{36}}}}}&{{\omega ^{{\rm{42}}}}}\\ {\rm{1}}&{{\omega ^{\rm{7}}}}&{{\omega ^{{\rm{14}}}}}&{{\omega ^{{\rm{21}}}}}&{{\omega ^{{\rm{28}}}}}&{{\omega ^{{\rm{35}}}}}&{{\omega ^{{\rm{42}}}}}&{{\omega ^{{\rm{49}}}}} \end{array}} \right){\left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}\\ {\rm{0}}&{\rm{0}}&{\rm{1}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}\\ {\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{1}}&{\rm{0}}&{\rm{0}}&{\rm{0}}\\ {\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{1}}&{\rm{0}}\\ {\rm{0}}&{\rm{1}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}\\ {\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{1}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}\\ {\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{1}}&{\rm{0}}&{\rm{0}}\\ {\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{0}}&{\rm{1}} \end{array}} \right)^{\rm{2}}}{\rm{ = }}{F_8}{P_8}^2\]

similiarly as before，we have

\[{F_8}{P_8} = \left( {\begin{array}{*{20}{c}} {\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}&{\rm{1}}\\ {\rm{1}}&{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{6}}}}&\omega &{{\omega ^{\rm{3}}}}&{{\omega ^{\rm{5}}}}&{{\omega ^{\rm{7}}}}\\ {\rm{1}}&{{\omega ^{\rm{4}}}}&{{\omega ^{\rm{8}}}}&{{\omega ^{{\rm{12}}}}}&{{\omega ^{\rm{2}}}}&{{\omega ^{\rm{6}}}}&{{\omega ^{{\rm{10}}}}}&{{\omega ^{{\rm{14}}}}}\\ {\rm{1}}&{{\omega ^{\rm{6}}}}&{{\omega ^{{\rm{12}}}}}&{{\omega ^{{\rm{18}}}}}&{{\omega ^{\rm{3}}}}&{{\omega ^{\rm{9}}}}&{{\omega ^{{\rm{15}}}}}&{{\omega ^{{\rm{21}}}}}\\ {\rm{1}}&{{\omega ^{\rm{8}}}}&{{\omega ^{{\rm{16}}}}}&{{\omega ^{{\rm{24}}}}}&{{\omega ^{\rm{4}}}}&{{\omega ^{{\rm{12}}}}}&{{\omega ^{{\rm{20}}}}}&{{\omega ^{{\rm{28}}}}}\\ {\rm{1}}&{{\omega ^{{\rm{10}}}}}&{{\omega ^{{\rm{20}}}}}&{{\omega ^{{\rm{30}}}}}&{{\omega ^{\rm{5}}}}&{{\omega ^{{\rm{15}}}}}&{{\omega ^{{\rm{25}}}}}&{{\omega ^{{\rm{35}}}}}\\ {\rm{1}}&{{\omega ^{{\rm{12}}}}}&{{\omega ^{{\rm{24}}}}}&{{\omega ^{{\rm{36}}}}}&{{\omega ^{\rm{6}}}}&{{\omega ^{{\rm{18}}}}}&{{\omega ^{{\rm{30}}}}}&{{\omega ^{{\rm{42}}}}}\\ {\rm{1}}&{{\omega ^{{\rm{14}}}}}&{{\omega ^{{\rm{28}}}}}&{{\omega ^{{\rm{42}}}}}&{{\omega ^{\rm{7}}}}&{{\omega ^{{\rm{21}}}}}&{{\omega ^{{\rm{35}}}}}&{{\omega ^{{\rm{49}}}}} \end{array}} \right){\rm{ = }}\left( {\begin{array}{*{20}{c}} {{I_4}}&{{D_4}}\\ {{I_4}}&{{\rm{ - }}{D_4}} \end{array}} \right)\left( {\begin{array}{*{20}{c}} {{F_4}}&0\\ 0&{{F_4}} \end{array}} \right)\]

**注：**如果你对上一步迷惑，这是正常的，不迷惑才不正常！因为根据单位根的性质，现在 
$F_8$中$\omega^2$才是$F_4$中的$\omega$ ，所以两个矩阵中的$\omega$并不是同一个数！(为何不用两个数以作区分呢？因为打字很费时间，将就着看吧...(我的我的))

**再注：**矩阵$D_4=diag(1,\omega,\omega^2,\omega^3)$是从$D_8$中来的，所以其中的 $\omega$ 是8次单位根。同理，$D_{2^{m-1}}$ 中的
 $\omega$是 $2^m$ 次单位根,懂？

*cont'd——*

\[{F_8}{P_8}^2 = \left( {\begin{array}{*{20}{c}} {{I_4}}&{{D_4}}\\ {{I_4}}&{{\rm{ - }}{D_4}} \end{array}} \right)\left( {\begin{array}{*{20}{c}} {{F_4}}&0\\ 0&{{F_4}} \end{array}} \right){P_8} = \left( {\begin{array}{*{20}{c}} {{I_4}}&{{D_4}}\\ {{I_4}}&{{\rm{ - }}{D_4}} \end{array}} \right)\left( {\begin{array}{*{20}{c}} {\left( {\begin{array}{*{20}{c}} {{I_2}}&{{D_2}}\\ {{I_2}}&{{\rm{ - }}{D_2}} \end{array}} \right)\left( {\begin{array}{*{20}{c}} {{F_2}}&0\\ 0&{{F_2}} \end{array}} \right){P_4}}&0\\ 0&{\left( {\begin{array}{*{20}{c}} {{I_2}}&{{D_2}}\\ {{I_2}}&{{\rm{ - }}{D_2}} \end{array}} \right)\left( {\begin{array}{*{20}{c}} {{F_2}}&0\\ 0&{{F_2}} \end{array}} \right){P_4}} \end{array}} \right){P_8}\]

从右往左看，排列矩阵不用管，中间是两个$F_4$的计算量，最左边考虑一次对角阵$D_4$ ..它总共需要的复数乘法次数 $O(F_8)=2×O(F_4)+4=12=\frac{8}{2}\log8$

所以可以归纳出：(归纳过程留作习题(**提示:**$2×(\frac{2^{k-1}}{2}  \log2^{k-1})+2^{k-1}=\frac{2^k}{2}\log2^{k}$))


|         | `DFT ` | `FFT `               |
|---------|--------|----------------------|
| `Order` | $N^2$  | $\frac{N}{2}\log{N}$ | 


 由$\mathop {\lim }\limits_{x \to \infty } \frac{{\log x}}{{{x^\varepsilon }}} = \mathop {\lim }\limits_{x \to \infty } \frac{1}{{{x^{1 + \varepsilon }}\ln 2}} = 0$
 ，可知FFT的运算量要小于$\frac{N^{1+\epsilon}}{2}$,而$\epsilon$是趋于$0$的，所以相当于从二次增长变成线性增长。

..

..

..


--**end**