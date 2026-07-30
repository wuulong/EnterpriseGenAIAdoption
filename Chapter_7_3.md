# 7.3 Database-First 中控控制面 (Meta DB)：APQC/ISO 條碼 physical 翻譯、全域實態總控表與 8 大數字狀態碼 [v1.7.1]

## 1. 平面 RAG 的終結：Database-First 混合架構 (`ADR-001`)

傳統基於純向量嵌入 (Vector Embedding) 的平面 RAG 在企業落地時面臨三大致命傷：
1. 切碎長文本 SOP 導致上下文斷裂。
2. 對數值、金額門檻與日期缺乏精確查詢能力。
3. 無法維護事務性 (ACID) 狀態。

v1.7.0 / v1.7.1 方法論提出 **Database-First 中控控制面 (`db/` 目錄)**，將關聯式 SQLite/PostgreSQL 資料庫作為底層紮實控制面。

---

## 2. Control Plane Meta DB 5 大實體資料表

在虛擬企業模板中，中控 DB 置於 `db/control_plane.sqlite`，包含 5 大核心 L3 控制面資料表：

```sql
-- 1. 外部系統介面閘道表
CREATE TABLE external_connectors (
    connector_id VARCHAR(64) PRIMARY KEY,
    system_name VARCHAR(100) NOT NULL,
    api_endpoint TEXT NOT NULL,
    auth_type VARCHAR(32) NOT NULL,
    status VARCHAR(20) DEFAULT 'ACTIVE'
);

-- 2. APQC / ISO 流程與實體 DB 表映射 (含 L0-L4 座標標籤)
CREATE TABLE apqc_data_mappings (
    mapping_id VARCHAR(64) PRIMARY KEY,
    apqc_code VARCHAR(32) NOT NULL,
    layer_level VARCHAR(10) DEFAULT 'L2',
    sop_id VARCHAR(64) NOT NULL,
    target_table VARCHAR(100) NOT NULL,
    target_api_action VARCHAR(100) NOT NULL
);

-- 3. Agent 權限與 RACI 控制表
CREATE TABLE agent_permissions (
    permission_id VARCHAR(64) PRIMARY KEY,
    agent_id VARCHAR(64) NOT NULL,
    apqc_code VARCHAR(32) NOT NULL,
    raci_role CHAR(1) NOT NULL,
    max_approval_amount DECIMAL(12,2) DEFAULT 0.00
);

-- 4. 執行與稽核軌跡日誌
CREATE TABLE execution_audit_logs (
    log_id VARCHAR(64) PRIMARY KEY,
    workflow_id VARCHAR(64) NOT NULL,
    agent_id VARCHAR(64) NOT NULL,
    action_performed TEXT NOT NULL,
    human_approved BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 5. 全域實體狀態總控調度表 (Entity State Engine [v1.7.1])
CREATE TABLE entity_state_ledger (
    item_id VARCHAR(50) PRIMARY KEY,          -- 全域唯一 ID (例: 'FNC-HR-001', 'SYS-OPS-GS', 'SOP-OPS-001')
    item_type VARCHAR(30) NOT NULL,          -- 項目類型 ('FUNCTION', 'SYSTEM', 'DOCUMENT', 'AGENT', 'WORKFLOW', 'TASK')
    item_name VARCHAR(100) NOT NULL,         -- 項目名稱 (例: '在宅醫師出診車輛準備 SOP')
    prefix_code VARCHAR(30),                 -- 所屬 Prefix (例: '05_OPS')
    apqc_id VARCHAR(30),                     -- 關聯 APQC (例: 'APQC-4.2')
    status INTEGER NOT NULL DEFAULT 10,      -- 數字狀態碼 (10:虛擬發想 ~ 80:修訂確認)
    memo TEXT,                               -- 人工審查備註 / 補充資訊 / 錯誤 Log
    meta_data TEXT DEFAULT '{}',             -- 擴充 Metadata (JSON 格式, 例: {"alignment_rate": 87.5})
    owner_agent_id VARCHAR(50),              -- 主責 Agent (例: 'AGT-OPS-001')
    last_updated_by VARCHAR(50),             -- 最後更新者 ('HYDRATION_ENGINE', 'HUMAN_ADMIN')
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 3. 八大生命週期數字狀態碼 (Status Integer Enum [v1.7.1])

為了極大化 SQL 查詢效能（支援 `WHERE status >= 30` 或 `ORDER BY status ASC`），`status` 欄位採數字碼管理：

- **`10` (虛擬發想 / VIRTUAL_IDEATION)**：初始發想與草案階段（預設初始值）。
- **`20` (虛擬確認 / VIRTUAL_CONFIRMED)**：虛擬層面規格、SOP 或二維清單審查確認。
- **`30` (真實對接啟動 / REAL_INTEGRATION_STARTED)**：開始接入真實企業/診所實體系統 (HIS/EMR/Sheet)。
- **`40` (對齊進行中 / ALIGNMENT_IN_PROGRESS)**：正在進行影子模式 (Shadow Mode) 比對與人機行為對齊。
- **`50` (已對齊 / ALIGNED)**：影子模式對齊度已達標 (>= 85%)。
- **`60` (已確認 / CONFIRMED)**：人類主管/顧問完成最終簽核與正式上線確認。
- **`70` (修訂中 / REVISION_IN_PROGRESS)**：正式上線資產發動重新修訂與維護。
- **`80` (修訂確認 / REVISION_CONFIRMED)**：修訂與變更內容完成二次審查確認。

---

## 4. 擬真極簡 IT 系統 (`SYS-xxx`) 與 API 驅動

為了讓對話討論與 Agent 動作具備實體掛載標的，將複雜企業 IT 簡化為二維系統代號 (`system_catalog.csv`)：
- `SYS-CORE-DB`: 中控 Meta DB (SQLite)
- `SYS-HR-GS`: 人事與員工資料庫 (Google Sheet)
- `SYS-RD-GIT`: 研發程式碼與 PRD 規格庫 (Git Repo)
- `SYS-FIN-GS`: 財務報支與請款單據庫 (Google Sheet)
- `SYS-PROC-GS`: 採購比價與供應商庫 (Google Sheet)
- `SYS-OPS-GS`: 營運現場與交付日誌庫 (Google Sheet)
- `SYS-MKT-CRM`: 行銷與客戶關係 CRM (Google Sheet)

當 SOP 提到「執行招募評估」時，`apqc_data_mappings` 自動將 `APQC-7.1` physical 翻譯為對 `SYS-HR-GS` 的 API/SQL 寫入動作，並於 `entity_state_ledger` 中將 `SOP-HR-001` 的狀態由 `20` (虛擬確認) 推升至 `30` (真實對接啟動) 乃至 `60` (已確認)，實現 100% 確定性驅動。
