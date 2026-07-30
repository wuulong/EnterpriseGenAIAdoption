# 📌 版本歷史：企業生成式 AI 轉型方法論

此檔案記錄《企業生成式 AI 轉型全書》及其周邊工具的演進歷程。

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

#### 2. 全書架構與大綱 (ToC.md) 對接修訂
- **章節修訂**：同步更新 1.3 節 (二維座標)、2.2 節 (Meta DB & SYS-xxx)、3.3 節 (3-Tier workflow)、4.1 節 (`ADR-005` 私有實例與影子模式) 及附錄 A Q7 虛擬企業影子測試。

---

## [v1.6.1] - 2026-07-08
### 🌟 Agentic Platform 平台化架構、治理工程 (Harness) 與生態合作落地 (Platformization, Harness Engineering & Ecosystem Collaboration)
本次升級將方法論跨入實體平台產品與商業實作。實作了地端自動脫敏去識別化、執行儀表板監控、剛性限制的治理工程與 Hook 攔截機制，並確立大腦與 SI 執行專業分工及獲利模型。

#### 1. Agentic AI Platform 平台架構與彈性部署
- **通用 Skill 共享庫 (3.4)**：定義如何將口袋技能格律化上傳至平台通用共享庫，防止重複造輪子。
- **雲地結合與自動去識別化 (4.1)**：敏感 Facts 地端留存與 Model Router，上雲前自動進行 PII 脫敏，並地端還原。
- **Execution Dashboard 儀表板 (4.2)**：實時呈報活動中 Task 運行流、Skill 被呼叫熱度 (Skill Heatmap) 與產出結果資產。

#### 2. 治理工程 (Harness Engineering) 與 Hook 攔截機制
- **治理工程與 Hook 攔截 (4.3 新增)**：藉由 before_action (高危動作與權限檢核) 與 after_action (產出品質與文件註解稽核) 的 Hook 攔截點剛性約束 Agent，以及基於 SDK 的多代理 MAS 循環修正 Loop。
- **子章節編號順延**：完成 4.4 法律認信與 4.5 回顧自測的序號物理順延更新。

#### 3. 轉型顧問、SOP 提取與三重獲利模型
- **顧問 SOP 提取與獲利模型 (5.3)**：重構有機賦能作業系統，還原 Wing Group 「戰術轉化器」核心概念。整合轉型顧問與 Node Map SOP 提取，並推出 GPU 機台部署、訂閱與流量費、顧問諮詢的三重獲利模型。
- **專業分工與生態合攻 (6.4 新增)**：解耦大腦顧問與 SI 執行方，並與 SDK 生態圈開發者進行技術合攻，順延 6.5 回顧自測。

---

## [v1.6.0] - 2026-07-08
### 🌟 三層人才架構、無感 Context 採集與 30步反思寫作流 (Three-Layer Talent, Frictionless Context Capture & 30-Step Reflection Flow)
本次升級實作了無感資料收集、創意防八股的寫作反思流，以及優化轉型組織架構的三層人才體系與指標百科更新。

---

## [v1.5.1] - 2026-06-25
### 🇹🇼 語感在地化與二維知識矩陣
... (其餘版本歷史保留)
