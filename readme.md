# 一根韭菜的定投实验笔记

## 缘起
下面这张图多次出现在笑来老师的课程中，它清晰展示了在一个大周期过程中，（价格【蓝色线】先跌后涨，呈现一个微笑型，称为一个大周期）投资总额与资产净值的变化情况。
多次看到这幅图后，我想进一步了解投资总额与资产净值在其它走势中的变化----好奇定投策略在各种各样的走势中如何表现，成为了这篇实验笔记的缘起。

<img src="https://github.com/AaronZhangAus/Deepdive-on-Regular-Investing-master/blob/master/xiaolai_graph.jpg" width="550" height="300">

## 实验方法/工具
实验使用Python 代码生成一段时期的标的价格，假设每周投资一个定值，计算出每周的投资总额及资产净值，最后将价格，投资总额，资产净值三条线同时画出。

IDE: PyCharm, version 2021.2
Python 3.9
硬件环境：
 
 
## 实验过程
整个过程由三部分组成，每个部分中具体展现了若干个走势，展示在各种浮动中定投策略的结果。每个部分在展示曲线以后，列出了我的观察与思考。

### 第一部分：五种特定走势
#### 持续上涨

<p float="left">
<img src="https://github.com/AaronZhangAus/Deepdive-on-Regular-Investing-master/blob/master/figures/7402.37.png" width="400" height="280"> 
<img src="https://github.com/AaronZhangAus/Deepdive-on-Regular-Investing-master/blob/master/collection/8917.24.png" width="400" height="280">
</p> 


以上两个图给中的上扬价格均为随机产生，幅度、频率随机。

#### 观察与思考：
1.	整体上涨的情况下，两个实验均显示较好的回报率（45.14%，16.57%）。
2.	上涨过程中的局部下跌对资产净值的影响很小，换句话讲，定投策略对短期的下跌不敏感，几乎在图表上观察不到局部下跌。
3.	两个图表同时显示，前半程的26周，资产净值与实际投资金额差距很小，在后半程逐渐拉开差距，开口增加。一种合理的解释应该是经过前半段的定投，到后面几周已经有了一定数量的股（币）数积累，从而当价格上涨时，资产净值会快速上升。
4.	由于左右两个标第价格是实验运行时随机生成，结束后价格曲线没有保存，无法重复实验来回答下面的问题：
a.	如果微调定投价格，每周定投120，150或80，50，52周后的回报率如何？
b.	如果调整定投频率，每两周投一次？每月投一次将如何影响回报率？
c.	标第价格不变时，有没有一个最优的定投值和频率的组合能够最大化回报率? 如果存在，如何找到。
（好在实验的第三部分是用真实的个股数据测试，能够用相同价格走势测试不同的定投值及定投频率）

 
#### 持续下跌
<p float="left">
<img src="https://github.com/AaronZhangAus/Deepdive-on-Regular-Investing-master/blob/master/collection/5451.47.png" width="400" height="280"> 
<img src="https://github.com/AaronZhangAus/Deepdive-on-Regular-Investing-master/blob/master/collection/4944.27.png" width="400" height="280">
</p>

#### 观察与思考：
1.	整体下跌的颓势下，即使定投策略也未能力挽狂澜。两个结果都表现亏损（-28.74%，-35.37%）
2.	两个实验中，前15周内的短期涨势对资产净值几乎没有任何提升。原因应该不难理解，因为初期持股（币）数很低，因此价格的变动对资产影响很小。
3.	与此同时在前25周内，定投策略虽然对局部上升反应麻木，但是有效抵抗了价格的剧烈下跌。尤其在图二中，10-18周期间价格已经狂坠至15000（50%）时，资产净值才开始稍稍走低于投资额度。
4.	两个实验的后半段中，由于定投一段时期带来的股（币）数积累，资产净值开始对价格下降愈发敏感，与投资总额的落差越来越明显。
5.	与All-IN BUY AND HOLD的投资方法（第一周内一笔投入所有资金，持有52周，不做任何操作）相比，定投策略显著地减少了损失 —— 第一个实验中标的价格已经由30000跌到了15000，损失50%，定投策略亏损-28.74%；第二实验价格由30000跌到8000，损失73%，定投策略亏损35.37%。
6.	这两个实验带来的另一个重要启示是，定投策略绝非万能，如果所选标的基本面表现不良，颓势已定，或是整体行业缩水萎缩，定投策略最多能够减少损失，不会带来收益。同时也现侧面验证了坚信标的能够长期稳步增长这样的信念，是定投策略发挥效力的底层根基。

#### 先涨后跌
<p float="left">
<img src="https://github.com/AaronZhangAus/Deepdive-on-Regular-Investing-master/blob/master/collection/5451.47.png" width="400" height="280"> 
<img src="https://github.com/AaronZhangAus/Deepdive-on-Regular-Investing-master/blob/master/collection/4944.27.png" width="400" height="280">
</p>

#### 观察与思考：
1.	首先从整体来观察，两个标的都表现出大幅下跌，第一个跌至几乎一半的价格，止于15000左右；第二个也表现出大致30%的下滑，停在了20000左右。与此同时，定投52周后，两个实验中的净资产也有较大的折损。比较起来，第一个实验中标的价格下跌近50%，定投亏损35.26%；第二实验价格下跌了三分之一左右（10000），定投亏损35.07%。这样的结果，二次验证了定投策略的降损能力，虽然无法完全止损，但是与上一次实验所示，当标的价格大幅走低时，定投的确能够不同程度地降低资产损失。
2.	接下来关注局部变化。两个实验中，由于在前15周内，所持股（币）数量很小，因此在价格上扬或下降时，资产受到很小的影响。两幅图中，将近30周时资产才最后无法抵抗价格的继续下滑，开始走低于投资值，随着价格的持续下潜，资产也加剧贬值。与投资额差距逐渐拉大的另一个原因，是越往后期，持股（币）数逐渐增加，这样对价格的变动反应会越加敏感。
 
#### 先跌后涨
<p float="left">
<img src="https://github.com/AaronZhangAus/Deepdive-on-Regular-Investing-master/blob/master/collection/5451.47.png" width="400" height="280"> 
<img src="https://github.com/AaronZhangAus/Deepdive-on-Regular-Investing-master/blob/master/collection/4944.27.png" width="400" height="280">
</p>

#### 观察与思考：
1.	在讨论上面的二幅图以前，再观察一下在开篇部分引用的笑来老师的这幅图（如下）。
 

2.	这里的两个实验几近完美地复刻了上图。最值得一提的是，52周的定投后，当标的价格经历大峡谷式的下坠，仅反弹到之前价格的60% （20000）时，资产回报已经高达42.62% 和54.2%。这是一个违背常识(counter-intuitive)的结果，不看图表，很难凭想象推断出。如果采用第一周ALL-IN的投资方法，52周后都出现严重亏损，而定投策略却带来惊喜的财产增长。
3.	这样的高回报，究其原因也不难理解。在两个实验中，经过前半程后，持股（币）数已经有了一定积累，尤其是在20周到30周的时间里，由于价格低廉，定投带来了持股（币）数的快速累积。因此在后半程的价格回潮中，资产对价格上扬非常敏感，随着价格攀升，资产快速地超越了投资值，在末尾高高翘起，冲刺出了可喜的回报率。
4.	与之前的实验一致，在前20周中，由于持股（币）数量低，价格的大幅下坠对资产的影响很弱。由此看来，定投策略对初期价格的跌坠反应麻木，起到了抵抗跌价、保值资产的作用。
5.	第一个实验在30周左右资产走势呈现出了洼地，第二个实验洼地也出现在20周左右。但是也是在资产洼地中（价格几近最低点），股（币）数实现了快速积累，资产洼地成为了随后快速增长的续力区，有如是跃起前做的深蹲起。

#### 锯齿型
<p float="left">
<img src="https://github.com/AaronZhangAus/Deepdive-on-Regular-Investing-master/blob/master/collection/5451.47.png" width="400" height="280"> 
<img src="https://github.com/AaronZhangAus/Deepdive-on-Regular-Investing-master/blob/master/collection/4944.27.png" width="400" height="280">
</p>

#### 观察与思考：
1.	两个实验中的标的价格波动频繁，呈锯齿状，绿色的资产净值在前半程几乎与投资金额没有差别，第一个实验中出现在3-4周时的价格下沉和12周时的上扬几乎对资产没有任何影响，原因很简单，前期的持股（币）数量很低。
2.	在两个实验的后半程，随着持股（币）数的累积，资产净值开始对价格走势愈发敏感，价格的升降开始在资产净值上带来波动。尤其是第二个实验在36周左右出现了最大幅的下跌，同时也带来了同时期资产的走低，但是幅度比价格下降幅度要小。
3.	52周后，第一个实验中经历了一系列的价格颠簸，资产净值稍低于投资金额 （-5.04%）; 值得一提的是第二个实验中，价格虽然没有恢复到原有价格（30000），但是资产净值仍然高于投资金额11.93%，这无疑地表明，对波动频繁的标的实施定投策略时，只要经过一段时期的持股（币）数积累，资产会对价格走势非常敏感----价格上涨，净值上升; 价格下探，净值也会下滑。换句话讲，只要标的价格长期看处于上扬，中前期的价格颠簸对后期盈亏影响不大。再一次印证笑来老师所说，标的的选择的确非常非常重要。

### 第二部分：完美大周期走势

第一部分测试了定投策略在五种走势中的表现，标的价格完全由代码随机产生，在数百次的模拟定投中，选择了典型的五种价格形态讨论。

这一部分的实验会更有趣，展示了定投策略在经历了一至三个大周期后表现的盈亏。这一部分的最后章节，详细记录了一个意外观察到的神奇表现。

分析图表之前，这里回顾一下定投人生群中对一个大周期的定义，当价格曲线下跌，之后上扬，展示出一个微笑开关时，称为经历了一个大周期。当然，两个大周期表示价格呈现两个连续微笑曲线，画了一个“W”。

标题中提到的完美大周期，指的是利用正弦函数sin(x)，模拟价格在52周内经历了一个完美对称的微笑曲线，始于30000，收于30000点，如下图所示：
 

#### 一个大周期

观察与思考：
1.	上面的第一个图中，代码模拟了标的价格52周内走出一个标准大周期 ---- 在正中26周时触底于15000，52周时回升至30000。中间图中的蓝色是投资金额的线性增长，橙色代表资产净值。下面的曲线代表了持股（币）数的增长。
2.	在模拟的52周里，每周投资100，因此第二个图中投资金额的蓝线呈线性增长。在前半程的26周中，明显看到资产净值一直低于投资金额，在26周标的价格降到最低时，资产净值也到达最低值。后半程开始后，资产净值与标的价格一同反弹，很快在36周左右追平投资金额，随后快速反超。最终在52周标的恢复原价时，资产净值获得了53.82%的收益。
3.	与第一周的ALL-IN策略相比，52周后，采用ALL-IN策略资产净值只能恢复到了初始价值，未能带来任何收益，而且全程处于亏损状态。如上所述，定投策略使资产净值在36周时就已投资金额持平，在后面阶段全面反超，有力地证明了实施定投策略一个大周期后，会带来相当可观的收益。
 
#### 二个大周期

1.	上面的图像中，标的价格在52周内经历了两个完美大周期，分别在13周和39周时，触底15000。
2.	两个大周期各自延续了26周。两个相同过程中，资产净值表现完全相同 – 前期探低，在13周和39周分别触底反弹，在价格恢复至30000时分别两次带来了很高的收益。为了进一步看清资产净值全程变化情况，我加入了新的代码加入了第四张资产收益率图（下面的第四张），展示了收益率在两个大周期中的变化情况，红色虚线表示收益率保平为0%。




3.	第四幅资产收益率图中最值得一提的是出现在26周和52周的两个相同的最高回报率以及在13周和39周出现的相同最低回报率。在后面的章节中我们会看到，每个大周期都会带来一模一样的资产收益变化，无论前面经历了多少个大周期，也无论后续重复多少个大周期。
 

#### 三个&四个大周期
  
#### 更多的大周期
 
## 第三部分：实际标的走势

### ETFs:
#### Bitcoin
#### QQQ
#### 银行股
#### 锂电股

### 公司股：
#### Facebook
#### Costco
#### Nvidia
#### McDonald’s

## 总结
## 后续工作
## 代码：https://github.com/AaronZhangAus/Deepdive-on-Regular-Investing-master

## 联系方式：
微信：阿荣（yang__au）
aaron.zhang.aus@gmail.com

 
 
## TOP 24 HIGHEST GAIN CRYPTOS FOR REGULAR INVESTING:
1.	DOGE-USD returns 3234.03
2.	LUNA1-USD returns 2816.71
3.	SOL1-USD returns 2092.4
4.	MATIC-USD returns 1570.09
5.	HEX-USD returns 1309.19
6.	ADA-USD returns 892.39
7.	BNB-USD returns 619.13
8.	ETC-USD returns 486.49
9.	AVAX-USD returns 381.19
10.	VET-USD returns 326.13
11.	THETA-USD returns 313.86
12.	ETH-USD returns 237.34
13.	DOT1-USD returns 182.9
14.	UNI3-USD returns 155.62
15.	XRP-USD returns 148.43
16.	TRX-USD returns 102.56
17.	BTC-USD returns 86.51
18.	XLM-USD returns 81.12
19.	FIL-USD returns 58.37
20.	BCH-USD returns 57.8
21.	LTC-USD returns 57.79
22.	LINK-USD returns 40.82
23.	USDT-USD returns 0.06
24.	USDC-USD returns -0.03
 
## TOP 50 HIGHEST GAIN STOCKS:
1.	OAS returns 11779.31
2.	WKSP returns 2000.1
3.	ZIVO returns 1596.6
4.	AADI returns 1596.52
5.	DTST returns 1418.89
6.	SPRT returns 873.16
7.	BYRN returns 789.7
8.	OCGN returns 718.88
9.	VTNR returns 631.11
10.	UGRO returns 627.89
11.	CTRM returns 571.11
12.	NURO returns 468.82
13.	SGOC returns 464.21
14.	MARA returns 456.99
15.	PMTS returns 364.24
16.	GSM returns 319.76
17.	IKNX returns 308.68
18.	BNGO returns 298.31
19.	SKINW returns 295.45
20.	CATB returns 293.73
21.	VRPX returns 290.11
22.	PDSB returns 284.07
23.	ESEA returns 279.2
24.	EDRY returns 278.28
25.	RIOT returns 274.29
26.	PRTA returns 271.74
27.	UONEK returns 259.32
28.	KOSS returns 255.84
29.	PECO returns 247.93
30.	SAVA returns 242.54
31.	AEHR returns 238.28
32.	NAOV returns 234.64
33.	MRIN returns 230.79
34.	ORMP returns 225.71
35.	MOXC returns 225.33
36.	PFMT returns 208.88
37.	NTLA returns 208.51
38.	VIRX returns 202.07
39.	PAVMW returns 198.31
40.	NEGG returns 195.5
41.	CDEV returns 189.53
42.	AMEH returns 187.06
43.	MRNA returns 186.66
44.	SCR returns 186.5
45.	BNTX returns 186.06
46.	MVIS returns 185.5
47.	HMHC returns 181.2
48.	CLSD returns 180.23
49.	JYNT returns 179.17
50.	MMAT returns 173.88
 
## TOP 50 HIGHEST GAIN ETFS:
1.	BDRY returns 145.35
2.	BNKU returns 125.59
3.	FAS returns 90.71
4.	DPST returns 69.31
5.	REMX returns 66.84
6.	TECL returns 62.58
7.	NRGU returns 60.66
8.	SOXL returns 55.17
9.	CURE returns 51.82
10.	GUSH returns 50.8
11.	ROM returns 49.49
12.	UYG returns 45.98
13.	DUSL returns 44.14
14.	LIT returns 43.79
15.	USD returns 41.99
16.	DIG returns 37.69
17.	FCG returns 35.75
18.	ERX returns 35.3
19.	PXE returns 34.37
20.	TPOR returns 33.25
21.	FRAK returns 32.41
22.	RXL returns 31.8
23.	IAI returns 30.95
24.	PSCE returns 29.94
25.	UXI returns 29.84
26.	BLOK returns 29.48
27.	XME returns 28.19
28.	UCYB returns 27.6
29.	PXI returns 27.41
30.	DFEN returns 27.3
31.	IEO returns 27.09
32.	HELX returns 27.04
33.	KCE returns 26.96
34.	GERM returns 26.36
35.	MLPO returns 25.9
36.	FTXO returns 25.27
37.	KBWB returns 25.22
38.	XOP returns 25.11
39.	FXO returns 25.1
40.	MLPR returns 24.64
41.	BUG returns 24.61
42.	RYF returns 24.1
43.	URA returns 24.0
44.	XLF returns 23.86
45.	VFH returns 23.71
46.	FNCL returns 23.69
47.	CLDL returns 23.41
48.	IUSS returns 23.29
49.	DFNL returns 22.97
50.	IYG returns 22.7
