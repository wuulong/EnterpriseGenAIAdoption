---
layer: L2
title: 職能邏輯載體：財務審計戰術庫
version: v1.0.0
type: Function Vessel (T-Pattern)
compatible_methods: v1.3.x
---
# 🧩 L2: 職能邏輯載體 (Function Vessel) - 審計 T-Patterns

## 1. 核心職能：異常專案勾稽 (Anomaly Detection)
*   **Context**: 處理大量健保申報明細與醫院資材庫存紀錄的交叉比對。
*   **Pattern**: 
    1. 提取申報專案程式碼。
    2. 比對庫存扣量與申報量之位數差。
    3. 標記偏差 > 5% 的專案。
*   **Artifacts**: 產出 `Audit_Anomaly_Report.csv`。

## 2. 職能邊界與決策邏輯
*   **判定規則**：優先判定重複申報與錯誤類別對應。
*   **規格化輸出**：使用 **[Lx] 格式** 標註所依據的審計條文。

## 3. 戰術演化 (Evolutionary Link)
*   **來源**：本戰術由實戰中之「口袋技能」提煉。
*   **更新觸發**：若 PE.04 (對位精準度) 連續三次低於 70%，則啟動戰術重構。
