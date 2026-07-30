# 📌 版本歷史：企業生成式 AI 轉型方法論

此檔案記錄《企業生成式 AI 轉型全書》及其周邊工具的演進歷程。

---

## [v1.7.1] - 2026-07-31
### 🌟 全域實態引擎 (Entity State Engine)、數字狀態碼 (10~80) 與全資產自動登錄
本次升級於中控控制面資料庫正式導入全域實體狀態總控表 (`entity_state_ledger`)、8 大數字狀態碼 (10~80) 與 JSON Metadata，解決虛擬企業落地與影子測試狀態監控問題。

#### 1. 全域實體狀態總控表 (`entity_state_ledger`) 與 8 大數字狀態碼 (7.3)
- **數字狀態碼 (Status Integer Enum)**：將狀態改為整數 10~80，包含 10 (虛擬發想)、20 (虛擬確認)、30 (真實對接啟動)、40 (對齊進行中)、50 (已對齊)、60 (已確認)、70 (修訂中) 與 80 (修訂確認)，極大化 SQL 查詢排序與區間篩選效能。
- **JSON Metadata 欄位 (`meta_data`)**：新增 `meta_data TEXT DEFAULT '{}'` 欄位，無痛寫入影子測試對齊率 (`alignment_rate`)、門檻金額與標籤。

#### 2. 全資產 100% 自動物理掃描與維運工具 (`manage_ledger.py scan`) (7.5)
- **全資產自動登錄**：發動 `manage_ledger.py scan` 物理掃描 7 大部門下所有 `functional_list.csv` (`FNC-xxx`)、`system_catalog.csv` (`SYS-xxx`)、`workflow_list.csv` (`WF-xxx`)、`_SOP/` Markdown 與 `Agents/` JSON，將全公司資產 100% 寫入中控 SQLite。
- **維運 CLI**：提供 `list`, `update`, `add`, `scan` 指令與 Terminal 中文標籤映射。

---

## [v1.7.0] - 2026-07-30
### 🌟 虛擬企業建模 (Virtual Enterprise)、雙軌融合 (Hydration) 與 GitOps 控制面實踐
本次升級正式將最新實證成果「虛擬企業模板 (virtual-enterprise-template) 與 SE-6D 系統工程」融入專書體系，建構完整「AI 原生虛擬企業 (Virtual Enterprise AI-Native Vessel)」的物理建構與部署運維框架。

#### 1. 新增「第 7 章 虛擬企業建模與 AI 原生架構實踐」 (Chapter 7.1 ~ 7.6)
- **Token 套利與雙軌融合 (7.1)**：提出「兩階段職能解耦 (Token Arbitrage)」，將廣泛情報探勘外包給 Deep Research/OSINT 工具，內建模型專注於 APQC PCF 與 ISO 9001/27001 確定性骨架之血肉填空 (Hydration)。
- **L0-L4 遺傳二維座標體系 (7.2)**：定義 `[DEPT]_[Lx]_[TYPE]_[NUM]` 座標 ID 格式，並實施 `L4 > L3 > L2 > L1 > L0` 脈絡堆疊後項覆蓋優先級。
- **Database-First 中控控制面 (7.3)**：建立 `db/control_plane.sqlite` 包含 4 大 L3 控制面資料表，將 APQC 條碼 physical 翻譯為 SQL/API 指令，連結 `SYS-xxx` 簡化系統與 `FNC-xxx` 職能。
- **正則對稱式 Standard 3-Tier `_workflow/` 管線 (7.4)**：全公司 7 大部門 (含 `00_CORE`) 一律實施 `Rules/` (剛性防線)、`Triggers/` (事件綁定)、`Workflows/` (步驟 YAML) 的 100% 正則對稱切法與 RACI 簽核門檻控管。
- **通用範本派生與私有實例隔離 (7.5)**：依據 `ADR-005` 實施通用範本 (Public Repo) 與私有標竿實例 (Private Repo) 嚴格隔離，透過一鍵派生腳本 (`instantiate_ve.py`) 與影子模式 (Shadow Mode) 85% 對齊度解鎖切換。
- **回顧與轉型成熟度自測 (7.6)**：提供 5 大維度之虛擬企業建模評估清單。

---

## [v1.6.1] - 2026-07-08
### 🌟 Agentic Platform 平台化架構、治理工程 (Harness) 與生態合作落地
... (其餘版本歷史保留)
