# 7.4 正則對稱式 3-Tier `_workflow/` 管線與 RACI 簽核門檻控管 [v1.7.0]

## 1. 職責完全解耦：Standard 3-Tier `_workflow/` 架構 (`ADR-003`)

為防止 AI Agent 在執行自動化管線時混淆資安控制點、事件與腳本步驟，全公司所有 7 大部門（包含 `00_CORE` 到 `06_MKT`）一律採用 100% 正則對稱之 3-Tier 解耦資料夾結構：

```plaintext
[DEPARTMENT]/_workflow/
├── Rules/                                             # 🛡️ 剛性防线 (Guardrails & ISO 27001)
│   └── [DEPT]_L2_RULE_001_guardrails.md
├── Triggers/                                          # ⚡ 事件觸發與 Agent Binding
│   └── event_triggers.json
├── Workflows/                                         # 📜 聲明式 YAML 劇本鏈
│   └── [DEPT]_L2_WORKFLOW_001_default.yaml
└── workflow_list.csv                                  # 📊 流程二維清單索引
```

---

## 2. 3-Tier 元件的物理分工

### ① `Rules/` (剛性控制防線)
定義資安 (ISO 27001)、敏感 PII 遮蔽與簽核金額門檻。代理人在執行任何動作前，平台強制將 `Rules/` 作為最高的 Guardrails 置頂注入。

### ② `Triggers/` (事件觸發與 Agent Binding)
定義 JSON 格式的事件映射：
```json
[
  {
    "event_id": "EVT-FIN-001",
    "event_name": "FIN_REIMBURSEMENT_SUBMITTED",
    "workflow_target": "Workflows/FIN_L2_WORKFLOW_001_default.yaml",
    "primary_agent": "AGT-FIN-001"
  }
]
```

### ③ `Workflows/` (聲明式步驟 YAML)
僅專注於定義極簡步驟鏈，維持高可讀性與維護性：
```yaml
name: FIN_L2_WORKFLOW_001_reimbursement_workflow
description: 財務費用報支審核與月度結帳劇本
trigger: FIN_REIMBURSEMENT_SUBMITTED
steps:
  - id: step_01
    name: 費用報支與發票合規性審核
    agent: AGT-FIN-001
  - id: step_02
    name: 月度財務試算與結帳
    agent: AGT-FIN-002
```

---

## 3. RACI 簽核門檻與 Human-in-the-loop (HitL) 攔截

在 `agent_permissions` 與 `Rules/` 中，強制執行 RACI 審核邊界：
- **Responsible (R)**：Agent 負責自動執行初步評估、單據掃描與草案撰寫。
- **Accountable (A)**：人類主管負責最終金額審核與責任承擔。
- **金額門檻攔截**：單筆金額超過預設門檻（如 NT$ 50,000）時，`workflow_list.csv` 的 `human_in_loop` 欄位標記為 `TRUE`，管線自動掛起並發送通知等待人類簽核。
