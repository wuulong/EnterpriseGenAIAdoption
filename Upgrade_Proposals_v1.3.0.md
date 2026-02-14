# 📄 v1.3.0 方法論升級提案書：戰術保真與配套設施深耕

**Milestone: Tactical Fidelity & Supporting Facilities (配套設施)**

## 第一階段：戰略與戰術的「動態解耦」 (Phase 1: Dynamic Decoupling)

### 1.1 核心質疑：解決「空洞化」與「半衰期」
在 v1.2.0 完成後，我們意識到主幹內容若過度陷入具體技術瑣事，會導致書籍半衰期過短。v1.3.0 的核心任務是將「底層戰略」與「實戰戰術」徹底分離。

### 1.2 戰術實作庫 (Tactics Library) 與 T-Patterns
建立獨立的 `tactics/` 目錄，專門存放具備「高實效、可複製」特質的職人經驗。
*   **戰術模板 (T-Pattern)**：包含 Context, Pattern, Artifacts, Failures, Reference。
*   **目標**：累積足夠厚度的戰術資產，作為未來「虛擬化」的燃料。

### 1.2.1 初始戰術樣本 (T-Patterns)
- [x] **T-5.2-Personal-Assistant-Sandbox**: 個人助理工作目錄與長期虛擬化習慣。
- [x] **T-2.1-Enterprise-Context-Bundle**: 企業背景組合包與業務起跑點。
- [ ] **T-2.1-Experience-Assetization**: 職人經驗 Markdown 化 Prompt 模式。
### 1.3 個人助理沙盒 (Personal Assistant Sandbox) - 長期虛擬化打底
*   **推動全員 PA 化**：每個人應習慣建立一個「雜項助理目錄」(如本專案的習慣)。
*   **數位身分生長**：透過在目錄中長期的 Agentic 對話，讓個人的決策邏輯、背景知識被 AI 吸收，這是在真實虛擬化前的「微型演練」。

---

## 第二階段：虛擬化前的「配套設施」(Supporting Facilities)

在進入更高階的轉型前，v1.3.0 必須優先處理以下配套：

1.  **身分初始化：企業背景組合包 (Minimum Viable Context, MVC)** [核心更新]：
    *   **定義**：優於技術 RAG 的「身分定義」程序。將企業身分、組織地圖、核心 SOP、資料字典與合規邊界，封裝為一組標準 MD 檔案。
    *   **效用**：解決 AI 「有技術、無身分」的漏洞，提供手動對話與代理人執行時的「基礎座標」。
2.  **技能資產化 SOP**：定義如何快速將「老師傅經驗」轉化為機器可讀的工具描述與 Prompt。
3.  **自動化評測對齊 (Eval-Alignment)**：建立不依賴人為直覺的自動評分機制，讓 Agent 具備自我質檢能力。
4.  **AgentOps 基礎設施強化**：穩定成本熔斷與幻覺監控機制。

---

## 第三階段：未來展望：虛擬鏡像與指揮官 (Archived Seeds)
*   **鏡像演練系統 (Mirror Playbook System)**：未來 2.x 的核心，目前僅作為設計材料存檔於 `design_materials/virtualization_seeds.md`。
*   **虛擬 COE 指揮官 (Virtual COE Agent)**：作為長期技術研發專案，暫不納入 v1.x 的正式落地清單。

---

**版本紀錄**：v1.3.0 正式提案 (2026-01-25) - 聚焦配套設施與戰術保真
