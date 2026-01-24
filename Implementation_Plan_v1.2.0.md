# 📋 v1.2.0 實施計畫書 (Implementation Plan)

## 1. 背景與目標
本計畫基於 `Upgrade_Proposals_v1.2.0.md` (Proposal)，旨在將「有機賦能 OS」的核心理念落實於《企業生成式 AI 轉型全書》系列文檔中。
*   **目標版本**：v1.2.0
*   **核心變更**：引入二維矩陣診斷、五大遺傳屬性、先行者網絡工作流、以及指標 2.0 體系。

---

## 2. 待更新檔案與動作項目 (Task List)

### A. 全域版本標定 (Global Versioning)
1.  **[x] `CoE_Implementation_Guide.md`**：
    *   `version` -> `v1.2.0`
    *   `compatible_book_range` -> `["v1.1.0", "v1.2.x"]`
2.  **[x] `Enterprise_Context_Schema.md`**：
    *   `version` -> `v1.2.0`
3.  **[x] `Upgrade_Proposals_v1.2.0.md`**：
    *   標註計畫已進入「實施階段」。

### B. 診斷架構升級 (Schema Update)
1.  **[x] `Enterprise_Context_Schema.md` - 第一章重構**：
    *   移除單一的「產業樣態分類」。
    *   新增「二維權重矩陣座標」檢核項。
    *   新增「企業 AI 遺傳密碼：五大屬性」描述欄位。
2.  **[x] `Enterprise_Context_Schema.md` - 組織評估優化**：
    *   加入「先行者密度」與「五星特質」檢核清單。

### C. 行動指南升級 (Guide Update)
1.  **[x] `CoE_Implementation_Guide.md` - 第零階段**：
    *   插入「五大屬性座標診斷」行動項。
2.  **[x] `CoE_Implementation_Guide.md` - Wing Group 循環**：
    *   插入「內容切片 (S-代號) 與非同步歸檔」SOP 行動項。
3.  **[x] `CoE_Implementation_Guide.md` - 結尾補充**：
    *   新增「流程有效性自我驗證」檢查清單。

### D. 核心書籍內容增補 (Book Chapters Update)
1.  **[x] `Comprehensive_Enterprise_GenAI_Transformation.md`** (或 `/Chapter_1_2.md`)：
    *   改寫診斷理論，引入矩陣與座標概念。
2.  **[x] `Comprehensive_Enterprise_GenAI_Transformation.md`** (或 `/Chapter_5_3.md`)：
    *   增補「五星特質」先行者網絡定義。
3.  **[x] 新增獨立檔案 `Metrics_Encyclopedia_Guide.md`**：
    *   撰寫「指標百科」初稿，包含四大頂層指標的建構方法。

---

## 3. 執行與驗證 (Verification)
1.  **一致性檢查**：確保「特質名詞」在 Schema 與 Guide 中完全對應。
2.  **鏈接檢查**：確保 Guide 中的參照點 (如 1.2) 指向已更新的內容。
3.  **案例回測預備**：選定 `V-CASE-001` 進行 Metadata 標定完成。

---

## 4. 進度追蹤
*   [x] 2026-01-25: 計畫書建立 (v1.2.0)
*   [x] 2026-01-25: 執行 Step A, B, C, D (完成)
