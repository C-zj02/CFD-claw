# 默认模板

模板文件位于 `assets/templates/*.json`。模板只提供可继续推进的默认值，不代表最终工程设置。

## quick_external_aero

适用：外流气动快速趋势评估。

默认：

- `analysis_type`: `external_aero`
- `fidelity`: `quick`
- 定常 RANS，可压缩，SST k-omega。
- 网格数量级约 50 万到 200 万。
- y+ 目标 30，使用壁函数。
- 输出 CL、CD、Cm、压力和马赫数云图。

## high_fidelity_external_aero

适用：需要更可靠气动力、压力分布或局部流动结构的外流评估。

默认：

- 网格数量级约 500 万以上。
- y+ 目标约 1，解析边界层。
- 残差目标更严格，监测量稳定窗口更长。
- 需要用户确认计算资源和预计耗时。

## intake_duct

适用：进气道、S 弯进气道、埋入式进气口、AIP 面特性。

默认指标：

- `total_pressure_recovery`
- `distortion`
- `mass_flow`
- `aip_total_pressure_uniformity`
- `lip_static_pressure`

关键边界：

- `inlets` 或 `farfield`
- `walls`
- `outlets`
- `aip`

重点加密：

- 进气唇口
- 弯道
- 分离风险区
- AIP 截面

## nozzle_exhaust

适用：收扩喷管、尾喷管、排气羽流。

默认指标：

- `mass_flow`
- `gross_thrust`
- `thrust_coefficient`
- `exit_pressure_ratio`
- `exit_mach_uniformity`

关键边界：

- `nozzle_inlet`
- `nozzle_throat`
- `nozzle_exit`
- `walls`

重点加密：

- 喉道
- 膨胀段
- 出口剪切层
- 激波风险区域

## coupled_inlet_engine_nozzle

适用：进气道、发动机面和喷管耦合的工程评估。

默认流程：

1. 先用 `dry_run` 确认边界命名和接口截面。
2. 分别生成进气道和喷管的监测量。
3. 通过 `custom_variables` 或 MATLAB 后处理计算安装损失、压力恢复和推力修正。
4. 真实执行前必须确认发动机边界或接口模型。

