# 7.2 團隊級載體與二維座標體系：L0-L4 遺傳感官與脈絡覆蓋優先級 [v1.7.0]

## 1. 團隊級載體 (The Vessel) 與 6 大職能劃分

虛擬企業為團隊 AI 協作的最高實體載體。在目錄組織上，劃分為全域核心與六大基礎營運部門：
- `00_Enterprise_Core`: 全域核心與總經理室 (`00_CORE`)
- `01_HR_Human_Resources`: 人力資源部 (`01_HR`)
- `02_RD_Research_Development`: 研發部 (`02_RD`)
- `03_FIN_Finance_Accounting`: 財務會計部 (`03_FIN`)
- `04_PROC_Procurement`: 採購供應部 (`04_PROC`)
- `05_OPS_Operations`: 營運交付部 (`05_OPS`)
- `06_MKT_Sales_Marketing`: 行銷業務部 (`06_MKT`)

---

## 2. 二維座標 ID 語法 (`[DEPT]_[Lx]_[TYPE]_[NUM]`)

為了解決大腦檢索時檔名混亂與語意飄移，v1.7.0 強制所有企業資產與文檔標註 **二維座標 ID**：

$$\text{Coordinate ID} = [\text{DEPT}]\_[\text{LAYER}]\_[\text{TYPE}]\_[\text{NUM}]$$

- **部門軸 ($\text{DEPT}$)**：`CORE`, `HR`, `RD`, `FIN`, `PROC`, `OPS`, `MKT`
- **階層軸 ($\text{LAYER}$)**：
  - `L0` (型態資料)：`TEMPLATE` (如 `HR_L0_TEMPLATE_001_job_description_template.md`)
  - `L1` (產業文明)：`FACT` (如 `CORE_L1_FACT_004_Enterprise_Glossary.md`)
  - `L2` (職能習慣)：`SOP`, `WORKFLOW` (如 `FIN_L2_SOP_001_reimbursement_sop.md`)
  - `L3` (企業真相)：`TRUTH`, `PROFILE`, `RACI`, `BOOK` (如 `CORE_L3_TRUTH_002_Master_Org_Chart.json`)
  - `L4` (個人專家)：`EXPERT`, `FEWSHOT` (如 `MKT_L4_EXPERT_001_sales_copilot.agent.json`)

---

## 3. 脈絡堆疊後項覆蓋優先級 (Context Stacking Priority)

代理人啟動並載入上下文時，強制遵循後項覆蓋前項的物理過濾邏輯：

$$\text{Context Resolution} = L4 \gg L3 \gg L2 \gg L1 \gg L0$$

```plaintext
+-------------------------------------------------------+
|  L4: 個人專家手感 (Expert Few-Shots) ──► 最高裁決權    |
+-------------------------------------------------------+
                           │ (覆蓋)
+-------------------------------------------------------+
|  L3: 企業真相與控制面 (Master Org / RACI / Meta DB)    |
+-------------------------------------------------------+
                           │ (覆蓋)
+-------------------------------------------------------+
|  L2: 職能習慣與 SOP (Department SOPs & Workflows)     |
+-------------------------------------------------------+
                           │ (覆蓋)
+-------------------------------------------------------+
|  L1: 產業文明與白皮書 (APQC PCF / ISO 27001 / book/)   |
+-------------------------------------------------------+
                           │ (覆蓋)
+-------------------------------------------------------+
|  L0: 基礎型態與 Markdown 模板                          |
+-------------------------------------------------------+
```

當 `L4` 個人專家手感與 `L2` SOP 衝突時，系統以 `L4` 現場老手之直覺為最高指導，但不得越過 `L3` RACI 與 `L1` ISO 資安剛性防線。
