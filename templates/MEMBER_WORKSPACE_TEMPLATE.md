# 📁 成員協作空間範本 (Member Workspace Template)

> **位置**：`/members/{member_id}/` (例如：`/members/wuulong/`)
> **目的**：建立個人沙盒與團隊中樞 (SyncHub) 的物理連結與緩衝區。

---

## 📂 個人對合空間 (`/members/{member_id}/`)

### 1. `inbound/` (團隊 -> 個人)
*   **用途**：這是由 **SyncHub** 負責寫入的情報站。
*   **內容**：
    *   `sync_report.md`：每日團隊進度對合小報。
    *   `signals/`：**別人給你的訊號**。例如：A 標註你的任務已可開始。

### 2. `outbound/` (個人 -> 團隊)
*   **用途**：成員在此處放置產出與「對外訊號」。
*   **內容**：
    *   `WL_YYMMDD.md` / `TR_XXXXXX.md`：產出成果。
    *   `notifications/`：**你給別人的訊號**。
        *   `done_task_A.md`：通知成員 B 快來領取成果。
        *   `broadcast_all.md`：給全隊的小啟示或提醒。

### 3. `staging/` (衝突緩衝區)
*   **用途**：當 SyncHub 偵測到「脈絡對撞」時，會在此處產出對比分析。
*   **內容**：
    *   `conflict_alert.md`：說明你的改動與哪位成員的改動衝突。
    *   `merging_suggestion.md`：AI 提供的邏輯融合建議。

---

## 🔄 互動程序

1.  **開始工作**：成員先看 `inbound/`，掌握團隊昨晚發生了什麼。
2.  **本地開發**：在個人的私有空間（Sandbox）進行。
3.  **提交產出**：將結果複製到 `outbound/` 並 Push。
4.  **對合檢查**：SyncHub 執行對撞分析。如果有問題，會把結果丟進你的 `staging/` 並在 Discord 標註你。
