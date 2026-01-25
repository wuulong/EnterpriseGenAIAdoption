# 📄 v1.3.0 方法論升級提案書：戰術保真與經驗反饋系統

**Milestone: Tactical Fidelity & Feedback Loop**

## 第一階段：戰略與戰術解耦 (Phase 1: Strategic & Tactical Decoupling)

### 1.1 核心質疑：解決方法論的「執行空洞」
在 v1.2.0 完成後，我們意識到主幹內容若過度陷入具體技術瑣事（如 API、介面、特定 Prompt 技巧），會導致主書半衰期過短且一般性不足。

### 1.2 戰術實作庫 (Tactics Library) 提案
建立獨立的 `tactics/` 目錄，用於建構具備高度特殊性的實作技巧與經驗。
*   **解耦邏輯**：戰略定義「坐標與方向」，戰術定義「操作與避坑」。
*   **反饋機制**：等到累積足夠戰術經驗（T-Lessons），再回頭評估是否需要更新戰略層級（Chapter 1-6）的內容。

### 1.3 戰術筆記標準模板 (T-Pattern)
每一篇戰術筆記需包含：
1.  **[Context] 問題場景**：遇到什麼挑戰？
2.  **[Pattern] 解決模式**：具體戰術做法。
3.  **[Artifacts] 實作資產**：具體的 Prompt、代碼片段、流程圖連結。
4.  **[Failures] 坑洞紀錄**：測試過哪些無效的方法？
5.  **[Reference] 歸因案例**：源自哪個實戰案例？

---

## 第二階段：預計提煉的初始戰術 (Initial Tactical Samples)
- [ ] **T-2.1-Experience-Assetization**: 職人經驗 Markdown 化 Prompt 模式。
- [ ] **T-3.3-MAS-Protocol**: 多代理人通訊與校驗協定實務。
- [ ] **T-2.2-Evidence-Retrieval**: 高合規場景下的 RAG 強化技術。

---

**版本紀錄**：v1.3.0 初始提案 (2026-01-25)
