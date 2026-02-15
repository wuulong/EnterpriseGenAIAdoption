# 🏥 實戰演練：手術室耗材異常審計 (Medical Audit Walkthrough)

**場景**：首席審計師陳大文啟動 Agent，對 2026 Q1 手術房耗材進行專案審核。
**版本**：v1.3.0 (對應 Layered Fractal Empowerment 方法論)

---

## 🚀 第一步：協議加載與脈絡對合 (Protocol Loading)

Agent 讀取 `Session_Manifest.yaml`，確認執行環境：
- **載體掛載**：L0 (Async), L1 (Compliance), L2 (Audit Logic), L3 (Star Hospital), L4 (Daven's Taste)。
- **優先序**：`L4 > L3 > L2 > L1 > L0`。
- **硬限制**：`L1_Hard_Filter: true` (啟動隱私攔截)。

> **Agent 內部狀態**：
> "正在加載陳大文的職人手感 (L4)，我將特別關注跨年度耗材波動。同時醫療法規層 (L1) 已鎖定，我會自動屏蔽所有患者真實姓名。"

---

## 🛡️ 第二步：資料讀取與 PII 攔截 (L1 Guard Action)

Agent 讀取 `raw_data_sample.csv`。

**執行動作**：
- 偵測到 `Patient_Name` 欄位包含：王小明、李大華、張美玲...。
- **L1 攔截觸發**：根據「PII 絕對屏蔽」規則，Agent 在記憶體處理時自動將姓名映射為 MASK 程式碼。

> **處理後片段**：
> `2026-02-01, OR-B2, [Patient_MASK_01], MISC-001, 麻醉誘導包, 1, 1`

---

## 🔍 第三步：職能邏輯運算與異常偵測 (L2 T-Pattern)

Agent 套用 `L2_Func_Audit_T_Pattern.md` 中的「異常專案勾稽」戰術。

**計算結果**：
1. **張美玲錄項 (MASK_03)**：`Quantity_Used: 5`, `Quantity_Invoiced: 10`。偏差率 **100%**。
2. **林志豪錄項 (MASK_05)**：`Quantity_Used: 20`, `Quantity_Invoiced: 40`。偏差率 **100%**。

**L3 動態加載 (Supplement)**：
- 讀取 `Audit_Policy_Supplement.md`，發現 `DRUG-99` 與「二月底核銷」均為紅色警戒項。

---

## 🖋️ 第四步：品位疊加與決策產出 (L4 Overlay)

根據 `L4_User_ChiefAuditor_Vibe.md`，陳大文對「跨年度挪用」極度敏感。

**Agent 推理**：
- "林志豪 (MASK_05) 的紀錄發生在 2026-02-28，正好是年度結算日。"
- "申報量整整是使用量的兩倍，且品項為重點監控的 DRUG-99。"
- "陳大文的 L4 風格要求直接列出 Table 並使用嚴厲語氣。"

---

## 📄 第五步：最終成果產出 (The Deliverable)

### 🏥 財務審計異常簽呈摘要 (Internal Use Only)
**TO**: 院長室 / 財務部  
**FROM**: 首席審計師陳大文助理 (AI Agent)

根據 2026-Q1 手術室耗材勾稽，以下專案存在重大異常，建議立即介入：

| 日期 | 案例編號 | 品項 ID | 名稱 | 數量差 | 偏差率 | 風險標籤 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 02-15 | [MASK_03] | DRUG-99 | 止痛針劑 | +5 | 100% | 輸入錯誤 |
| 02-28 | [MASK_05] | DRUG-99 | 止痛針劑 | +20 | 100% | **跨年度調撥嫌疑** |

**職人裁決 (L4 Deviation Insight)**：
特別關注 02-28 的記錄。該筆交易申報量與扣庫存數完全不符。考慮到適逢年度預算結算日，此舉高度疑似為「預算耗盡」目的之虛報領用。

**合規聲明 (L1 Filter applied)**：
本報表已屏蔽 PII 敏感資訊。原始資料存於安全審計區 [Audit_Log_Reference_7782]。

---

## 🔄 第六步：方法論演化 (Evolution Loop)

**戰術回填**：
陳大文在審核此報告後存檔。Wing Group 偵測到此案例，將「日期跨年度 + 重點藥品代號 + 雙倍誤差」定義為一個新的偵測模式，並回填至 **`L2 職能庫`**，供全院代理人升級。
