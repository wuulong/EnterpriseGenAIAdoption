# 🛠 團隊工具使用與對齊指引 (Team Tools Usage & Sync Guide)

> **說明**：本檔案是 `TEAM_HANDBOOK` 的深度補充，針對各種標準工具提供具體的「使用規範」與「對齊建議」，確保超小型團隊的數位環境整潔且具備高度同步性。

---

## 1. 📂 Git (版本控制與協作)
*   **預執行原則 (Safe Start)**：每次開始工作前，請務必先執行 `git pull`，避免產生不必要的 Conflict。
*   **Commit 規範**：
    *   格式：`[任務ID] 動詞: 簡短描述` (例如：`[T260224-01] Update: 修正說明書範本`)。
    *   意義：這不只是備份，而是給 AI 與隊友看的「開發歷程」。
*   **大檔案禁令**：禁止直接上傳超過 50MB 的二進位檔案（圖資、影片），請將其放入 Google Drive 並在檔案中留連結。
*   **Undo 協議**：若 AI 大改檔案後出錯，請先暫停，查看 `git log` 並使用 `git checkout [hash]` 回溯，不要試圖在錯誤基礎上修補。

---

## 2. 📝 Markdown (檔案編修)
*   **編輯器對齊**：建議統一使用 VS Code 或 Obsidian，並安裝 Markdown Lint 插件。
*   **相對路徑原則**：連結檔案或顯示圖片時，**絕對禁止**使用本地絕對路徑（如 `C:\Users\...`），必須使用相對於 Repo 根目錄的路徑。
*   **縮排與格式**：統一使用 **2 個空格** 縮排，避免 Git Diff 產生大量的空白字元衝突。
*   **前端元資料 (YAML Frontmatter)**：重要檔案頂部應包含標題、日期、作者、狀態。

---

## 3. 💬 Discord & Line (即時通訊)
*   **頻道分流 (Discord)**：
    *   `#announcement`：僅發布正式公告。
    *   `#task-discussion`：針對具體工作專案的討論。
    *   `#random-ideas`：碎碎念與靈感發想。
*   **討論串機制 (Threads)**：針對單一問題的深入討論，**必須開啟 Thread**，避免洗掉主頻道的對話。
*   **通知設定**：非緊急事項不要 @all 或 @everyone。看到重要討論請用 Emoji (👍/👀) 回應，代表「已收到且理解」。

---

## 4. 🤖 AI 助手 (Antigravity & LLMs)
*   **透明度原則**：如果開發出一個很好用的 Prompt，請將其記錄在專案的 `PROMPTS.md` 中。
*   **反饋機制**：當 AI 誤解指令時，請及時修正並在 `work-logs` 記錄「錯誤模式」，防止團隊其他人踩雷。
*   **交接 (Handover)**：當你負責的部分做完要交給下一位成員時，請叫 AI 產出一份 `Briefing`，說明目前的進度與剩餘風險。

---

## 5. 📹 視訊會議 (Google Meet / Zoom)
*   **錄影與逐字稿**：涉及決策的會議**必須錄影**或開啟自動逐字稿功能。
*   **會後煉金**：會議結束後 TBD (建議儘速)，應由 AI 或負責人將逐字稿轉化為 `Decision_Alignment_Sheet.md` 並 Push 到 Git。

---

## 6. ☁️ Google Drive (資源存儲)
*   **命名協議**：檔案命名格式 `YYYYMMDD_專案名_檔案描述_vX`。
*   **權限管理**：確保設定為「知道連結的人皆可檢視」，並將連結貼入對應的 Markdown 檔案中，實現「檔案讀取、雲端取貨」。

---
*Last Updated: 2026-02-24 | Designed for Nano-Squad Efficiency*
