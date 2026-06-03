# 边界命名规范

边界命名是导入模型前的必要确认点。不要依赖“自动识别”替代用户确认。

## 通用命名

- `farfield`：外流远场或计算域外边界。
- `wall_*`：固壁，例如 `wall_fuselage`、`wall_duct`、`wall_nozzle`。
- `symmetry_*`：对称面。
- `periodic_*`：周期面。
- `interface_*`：耦合接口。

## 进气道

建议名称：

- `inlet_capture`：进气捕获面或入口外边界。
- `wall_lip`：唇口壁面。
- `wall_duct`：进气道内壁。
- `aip` 或 `engine_face`：发动机面/AIP 监测截面。
- `outlet_engine_face`：若作为出口边界使用的发动机面。

进气道最低要求：

- 至少有 `walls`。
- 必须有 `aip` 或等价监测截面。
- 必须有入口/远场和出口/发动机面定义。

## 排气喷管

建议名称：

- `nozzle_inlet`：喷管入口/总压总温给定面。
- `nozzle_throat`：喉道截面或监测区。
- `nozzle_exit`：喷管出口。
- `wall_nozzle`：喷管壁面。
- `plume_farfield`：喷流外边界。

喷管最低要求：

- 必须有 `nozzle_inlet`。
- 必须有 `nozzle_exit`。
- 必须有 `walls`。
- 高精度喷流评估应定义外部远场或羽流计算域。

## 外流气动

建议名称：

- `farfield`
- `wall_body`
- `wall_wing`
- `wall_tail`
- `symmetry_xz`

最低要求：

- 必须有 `farfield`。
- 必须有至少一个 `wall`。
- 气动力输出需要参考面积、参考长度和力矩参考点。

## 命名检查策略

检查时按 `analysis_type` 判断缺失项：

- `external_aero`：`farfield`、`walls`、参考量。
- `intake_duct`：`aip`、`walls`、入口/出口或远场/发动机面。
- `nozzle_exhaust`：`nozzle_inlet`、`nozzle_exit`、`walls`。
- `coupled_propulsion`：同时满足进气道和喷管的接口定义。

缺失边界时进入 `awaiting_confirmation`，不要生成 `execute` 命令。

