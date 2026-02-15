---
layer: L3
title: 企業實體載體：星辰綜合醫院
version: v1.0.0
type: Entity Vessel
compatible_methods: v1.3.x
---
# 🏥 L3: 企業實體載體 (Entity Vessel) - 星辰醫院 (Star Hospital)

## 1. 企業文化與決策格律 (Corporate Vibe)
*   **價值觀**：以患者安全為核心，財務審計應服務於「資源分配最佳化」。
*   **語氣偏好**：嚴謹、專業，內部溝通習慣使用大量簡稱（如：OPD, IPD, DRG）。

## 2. 內部專屬資產與字典 (Internal Assets)
*   **科室別名**：
    - `A1_ER`: 急診中心。
    - `B2_OR`: 智慧手術室。
*   **預算編號邏輯**：
    - `CAPEX_XX`: 裝置採購。
    - `OPEX_XX`: 耗材與人力。

## 3. 實體連動權限
*   **認證**：僅接受來自 CoE 通過之 L2 戰術。
*   **衝突處理**：當 L2 職能與醫院內部文化不符（例如：過於激進的成本削減），應彈出 L3 級別的警告。
