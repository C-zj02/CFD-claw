---
name: aircraft-design-skill
description: 面向固定翼飞行器总体设计的 feasibility-first 交互技能. 用于自然语言需求抽取, Class I/II 重量与任务闭合, 约束诊断, 模型覆盖检查, 用户确认后的有界修正, 完整复验, 参数化几何, 报告和可视化. 当用户要求设计飞机或无人机, 判断参数是否可行, 协商修改矛盾指标, 比较候选方案, 或解释总体设计结果时使用.
allowed-tools:
  - Bash
  - Read
  - Glob
---

# Aircraft Design Skill

本技能以项目 `src/design_intake` 的版本化需求契约为入口, 以 `src/design_execution` 和 `external/aircraft-design-skill` 的确定性求解器为计算后端. 不允许跳过预检直接用求解器结果回答可行性问题.

## 强制流程

对设计请求严格执行以下顺序:

1. 将自然语言抽取为 `DesignIntent`, 统一 SI 单位, 保留原文和字段来源.
2. 将字段分类为 `hard_constraint`, `soft_goal`, `design_variable` 或 `technology_assumption`, 并标记 `locked`.
3. 执行 deterministic preflight, 同时检查缺失信息, 跨字段矛盾和模型覆盖.
4. 按诊断状态行动. `needs_clarification` 时提问; `unsupported` 时报告模型缺口; `contradictory_requirements` 或 `repairable` 时展示修正提案和影响; `infeasible` 仅用于已收敛模型的有界搜索耗尽结果.
5. `diagnosis.ready_for_solver=true` 只表示预检具备确认条件. 只有当前 revision 得到用户确认, 且服务端状态为 `confirmed=true` 和 `can_submit=true` 时, 才能提交确定性求解.
6. 每次接受修正后创建新 revision, 重新 preflight. 用户在对话中说“把某参数改为某值”时, 基于当前 revision 生成逐字段 diff, 不得丢弃旧约束后创建残缺的新 intent.
7. 每次求解器内修正后从 Class I 开始完整复验所有阻断阶段和约束. 求解失败时将失败约束, 实际值和裕度回灌为未确认 child revision; 只生成白名单内有证据的修改提案.
8. 按验证证据报告结果等级, 未满足交付门槛时不得称为可行方案.

完整状态机和执行入口见 [workflow.md](references/workflow.md).

## 不可违反的规则

- 用户硬约束和任何 `locked=true` 字段不得静默修改. 修改必须形成 `ChangeProposal`, 由用户明确确认.
- `unsupported` 表示当前模型缺失或超出适用域, 不等于 `infeasible`, 也不能作为物理不可行的证据.
- `diagnosis.ready_for_solver` 只表示预检通过, 不构成求解授权, 更不表示已经工程可行.
- 未经来源和适用域证明, 不得通过降低 `cd0`, 提高 `oswald_e`, 降低 TSFC/BSFC 或提高材料性能制造乐观解.
- 搜索耗尽时报告未找到可行解和失败约束, 不得删除约束, 篡改报告或把最后一次迭代值包装为方案.
- “继续”, “直接计算”或类似文本不是 revision 确认. 只有服务端记录的确认与 solver submission 审计可以授权求解和工作台归属.
- `geometry.obj`, `geometry_3d.html` 和配套图片只是展示资产. 它们不证明已执行 OpenVSP/VSPAERO, 高保真气动, 结构, 疲劳, 气动弹性, 制造或适航验证.

## 按需读取

- 先读取 [workflow.md](references/workflow.md) 执行总体状态机.
- 构建或修改 intent 时读取 [input-schema.md](references/input-schema.md).
- 判断某项需求是否有模型支持时读取 [model-coverage-matrix.md](references/model-coverage-matrix.md).
- 发生提问, 修改或确认时读取 [dialogue-policy.md](references/dialogue-policy.md).
- 声明结果可行性或交付等级前读取 [validation-levels.md](references/validation-levels.md).

按阶段加载对应 reference; 不要在需求尚未进入该阶段时加载无关细节.

## 输出

向用户明确列出当前需求 revision, 硬约束, 可调整变量, 技术假设, 模型缺口, 用户已接受的修改, 求解状态, 阻断约束裕度, 验证等级和剩余验证缺口. 结果文件必须给出实际路径; 未实际运行的工具不得声称已运行.
