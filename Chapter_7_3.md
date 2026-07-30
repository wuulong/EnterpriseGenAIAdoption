# 7.3 Database-First 中控控制面 (Meta DB)：APQC/ISO 條碼 physical 翻譯與 SQL/API 指令驅動 [v1.7.0]

## 1. 平面 RAG 的終結：Database-First 混合架構 (`ADR-001`)

傳統基於純向量嵌入 (Vector Embedding) 的平面 RAG 在企業落地時面臨三大致命傷：
1. 切碎長文本 SOP 導致上下文斷裂。
2. 對數值、金額門檻與日期缺乏精確查詢能力。
3. 無法維護事務性 (ACID) 狀態。

v1.7.0 方法論提出 **Database-First 中控控制面 (`db/` 目錄)**，將關聯式 SQLite/PostgreSQL 資料庫作為底層硬核控制面。

---

## 2. Control Plane Meta DB 4 大實體資料表

在虛擬企業模板中，中控 DB 置於 `db/control_plane.sqlite`，包含 4 大核心 L3 數據表：

```sql
-- 1. 外部系統介面閘道表 (連結 SYS-xxx)
CREATE TABLE external_connectors (
    connector_id VARCHAR(64) PRIMARY KEY,
    system_name VARCHAR(100) NOT NULL,
    api_endpoint TEXT NOT NULL,
    auth_type VARCHAR(32) NOT NULL,
    status VARCHAR(20) DEFAULT 'ACTIVE'
);

-- 2. APQC 流程條碼 physical 翻譯表
CREATE TABLE apqc_data_mappings (
    mapping_id VARCHAR(64) PRIMARY KEY,
    apqc_code VARCHAR(32) NOT NULL,       -- 如: APQC-7.1 (L1)
    layer_level VARCHAR(10) DEFAULT 'L2',
    sop_id VARCHAR(64) NOT NULL,          -- 如: HR_L2_SOP_001
    target_table VARCHAR(100) NOT NULL,
    target_api_action VARCHAR(100) NOT NULL
);

-- 3. Agent 權限與 RACI 控制表
CREATE TABLE agent_permissions (
    permission_id VARCHAR(64) PRIMARY KEY,
    agent_id VARCHAR(64) NOT NULL,
    apqc_code VARCHAR(32) NOT NULL,
    raci_role CHAR(1) NOT NULL,            -- R, A, C, I
    max_approval_amount DECIMAL(12,2) DEFAULT 0.00
);

-- 4. 執行與稽核軌跡日誌表
CREATE TABLE execution_audit_logs (
    log_id VARCHAR(64) PRIMARY KEY,
    workflow_id VARCHAR(64) NOT NULL,
    agent_id VARCHAR(64) NOT NULL,
    action_performed TEXT NOT NULL,
    human_approved BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 3. 擬真極簡 IT 系統 (`SYS-xxx`) 與 API 驅動

為了讓對話討論與 Agent 動作具備實體掛載標的，將複雜企業 IT 簡化為二維系統代號 (`system_catalog.csv`)：
- `SYS-CORE-DB`: 中控 Meta DB (SQLite)
- `SYS-HR-GS`: 人事與員工資料庫 (Google Sheet)
- `SYS-RD-GIT`: 研發代碼與 PRD 規格庫 (Git Repo)
- `SYS-FIN-GS`: 財務報支與請款單據庫 (Google Sheet)
- `SYS-PROC-GS`: 採購比價與供應商庫 (Google Sheet)
- `SYS-OPS-GS`: 營運現場與交付日誌庫 (Google Sheet)
- `SYS-MKT-CRM`: 行銷與客戶關係 CRM (Google Sheet)

當 SOP 提到「執行招募評估」時，`apqc_data_mappings` 自動將 `APQC-7.1` physical 翻譯為對 `SYS-HR-GS` 的 API/SQL 寫入動作，實現 100% 確定性驅動。
