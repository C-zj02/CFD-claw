# 公式与符号约定

读取时机：执行气动导数拟合、推阻特性、安定性、配平、进气道、发动机、喷管或安装推力运算时，只加载相关小节。

## 通用数据处理

- 角度导数默认同时输出 `每弧度` 和 `每度`。若原始迎角或侧滑角为度，线性拟合前转换为弧度。
- 同一拟合不得混合不同 Mach、高度、构型、舵偏、襟翼状态、外挂状态或参考面积。
- 线性拟合至少报告样本数、拟合区间、斜率、截距、R2 或残差趋势。样本太少时标注为估算。
- 数值单位必须写在列名或表头中，例如 `CL_alpha (1/rad)`、`TSFC (kg/N/s)`。

## 升力线斜率

使用小迎角线性区间拟合：

```text
CL = CL0 + CL_alpha * alpha
alpha0 = -CL0 / CL_alpha
```

输出：

- `CL_alpha`：升力线斜率，优先每弧度。
- `CL0`：零迎角升力系数。
- `alpha0`：零升迎角。
- `线性区间`：例如 `alpha = -2 deg 到 8 deg`。

## 推阻特性

常用阻力极曲线：

```text
CD = CD0 + k * CL^2
e = 1 / (pi * AR * k)
D = q * S * CD
T_required = D
P_required = D * V
L/D = CL / CD
```

输出 `CD0`、`k`、`Oswald效率因子 e`、`最大升阻比`、`所需推力/功率`、`推阻裕度`。若推力曲线与阻力曲线工况不同，先修正或明确不可直接比较。

## 纵向安定性

典型线性表达：

```text
Cm = Cm0 + Cm_alpha * alpha + Cm_delta_e * delta_e
static_margin = -Cm_alpha / CL_alpha
```

约定：若 `Cm` 关于质心取矩且 `alpha` 为弧度，通常 `Cm_alpha < 0` 表示纵向静稳定。`static_margin` 为平均气动弦比例。若数据采用不同轴系或力矩参考点，先转换或声明口径。

## 配平能力

先由飞行状态求所需升力系数：

```text
CL_required = W / (q * S)
delta_e_trim = -(Cm0 + Cm_alpha * alpha_trim) / Cm_delta_e
```

输出：

- 配平迎角或配平升力系数。
- 配平舵偏角及其是否落在允许舵偏范围内。
- 舵效裕度：到上/下限的剩余角度。
- 若 `Cm_delta_e` 符号或舵偏正方向不明，先确认。

## 横航向安定性

常用导数：

```text
CY = CY0 + CY_beta * beta
Cl = Cl0 + Cl_beta * beta
Cn = Cn0 + Cn_beta * beta
```

典型静稳定判据取决于轴系和侧滑角定义。在常见航空符号约定下，`Cn_beta > 0` 表示方向静稳定，`Cl_beta < 0` 通常表示正的上反效应。若来源未说明正方向，不给强判定，只给导数和需确认项。

## 进气道总压恢复

```text
pi_d = Pt_exit / Pt_free_stream
pressure_loss = 1 - pi_d
```

按 Mach、迎角、侧滑角、流量系数或捕获流量分组。若涉及畸变，列出使用的畸变指标和测点截面，不能把平均总压恢复当作畸变指标。

## 发动机推力与耗油率

```text
SFC = fuel_mass_flow / thrust
TSFC = fuel_mass_flow / net_thrust
fuel_flow = TSFC * net_thrust
```

输出时写清单位，例如 `kg/(N*s)`、`kg/(daN*h)`、`lbm/(lbf*h)`。推力随高度、Mach、温度和进气条件变化，不能把海平面静推力直接用于高空高速工况。

## 喷管推力系数

火箭或高压喷管常用：

```text
CF = F / (pc * At)
```

也可能使用 `实际推力 / 理想推力` 作为效率口径。先确认 `pc`、`At`、环境压强、膨胀比和推力定义。不同口径不可混表比较。

## 安装推力

两种常见口径：

```text
F_installed = F_gross - D_ram - D_inlet - D_nozzle - D_nacelle - other_losses
F_installed = eta_install * F_uninstalled
```

优先使用用户或资料给定的口径。若只做方案级估算，可用安装效率范围，但必须标为工程假设，并说明包含或不包含进气道压损、短舱阻力、喷管损失和引气/功率提取。
