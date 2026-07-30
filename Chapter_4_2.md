# 4.2 AgentOps 與效能監控：Execution Dashboard 設計、Skill 生命周期與 Task 監控

當企業在生產環境中部署了多代理系統與平台底座後，維運面臨前所未有的挑戰：**「我們如何實時掌握數百個數位員工的運作狀態、算力消耗與實質產出？」**

為此，在 v1.6.1 中，我們將 AgentOps 核心展示層升級為 **Execution Dashboard (執行儀表板)**，並提供 Skill 生命周期與 Task 監控的實作規範。

---

## 4.2.1 執行儀表板 (Execution Dashboard) 的設計實作

**Execution Dashboard** 是平台提供給企業管理者的「戰情監控室」，旨在將不可見的 AI 推理過程實體化為可量化的指標看板：

1.  **Task (任務) 運作流監控**：
    *   **監控指標**：當前正在活動中的 Task 總量、平均任務響應時間、以及 Task 的最終完成率 (Completion Rate)。
    *   **視覺化呈報**：實時以時間軸或節點地圖 (Node Map) 的形式，呈現當前進行中 Task 的推理進度，並在發生阻礙或 `HALT` 例外（如資料超限）時以紅色警告閃爍，等待人類管理者點擊處理。
2.  **Skill 被呼叫熱度與分佈 (Skill Heatmap)**：
    *   **監控指標**：統計各部門通用 Skill（如 BOM 比對、合約合規稽核、語義翻譯）被代理人調用的頻次、每次呼叫的算力成本（Token Cost）以及平均耗時。
    *   **業務價值**：協助 CoE 主管識別「高價值 Skill」與「低頻無效 Skill」，作為持續最佳化 Skill Map (技能地圖) 的量化依據。
3.  **實體產出成果管理**：
    *   在 Dashboard 上實時呈現 Agent 產出的具體檔案資產，包含自動產出的文案、BOM 差異比對圖表、程式碼檔案等，並建立版本追蹤，方便 Manager of Agents 進行檢索與 Audit。

---

## 4.2.2 協作流追蹤與死鎖監控

不同於單一 AI 的機率性行為，多代理協作的交互路徑是網狀且動態的：
*   **交棒路徑追蹤 (Handoff Traceability)**：記錄任務從人類分配到 Orchestrator，再分派給特定職能 Agent (如 `RD_L3`)，最後交棒給 `MFG_L2` 品檢 Agent 的完整路徑，方便故障定位。
*   **死鎖偵測 (Deadlock Detection)**：監控 Agent 之間的通訊，若發現 A 與 B 之間針對同一任務的交互次數超過通訊格律限制 (如 Max Rounds = 3) 仍未收斂，必須即時觸發 `HALT` 警報，防止雲端算力空轉。

---

## 4.2.3 成本控管與 Token 熔斷

多 Agent 併行任務是極其消耗算力的：
*   **Token 熔斷與輪次限額**：除了任務總 Token 預算限制，還必須限制協作的最大對話輪次。一旦 Agent 陷入邏輯死循環或嘗試無效工具調用，強制熔斷並呼叫人類主管。

---

## 4.2.4 Skill 的 CI/CD 與生命週期管理 (Skill Lifecycle)

當企業內部的 Agent 分別掛載了不同的業務 Skill 節點後，我們必須將 Skill 視為軟體程式碼，納入生命週期管理：
*   **語義版本控制 (Semantic PR)**：當業務程序改變（例如差旅核銷門檻從 3000 元降至 2000 元）時，人類 Builder 不應手動修改生產環境中的 Prompt，應在 Git 上發起一個 Pull Request (Semantic PR)，修改 Skill 對應的 System Prompt 原始檔。平台會自動將此 PR 掛載到「黃金測試集」進行模擬跑分，驗證其是否引發合規或效能下降，通過後才自動合併發布到生產環境。

### 結論
Execution Dashboard 將抽象的 Agent 推理與 Skill 調用轉化為企業主的實體監控儀表，結合 Skill 的 CI/CD 與 Token 熔斷，為企業在算力通膨時代提供了長治久安的 AI 運維架構。

在下一節 4.3 中，我們將探討如何藉由 **治理工程 (Harness Engineering)** 與 **Hook 機制** 來剛性約束這些代理人的執行行為。
