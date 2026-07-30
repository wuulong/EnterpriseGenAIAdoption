# 7.6 本章回顧與自測：虛擬企業建模評估與轉型成熟度檢核 [v1.7.0]

## 1. 核心觀念回顧 (Core Key Takeaways)

1. **Token 套利與兩階段解耦**：避免直接複製舊官僚程序。先外包 OSINT/Deep Research 搜集血肉，再由內建大腦進行 APQC/ISO 確定性骨架融合。
2. **L0-L4 遺傳二維座標**：以 `[DEPT]_[Lx]_[TYPE]_[NUM]` 標註資產點位，遵循 `L4 > L3 > L2 > L1 > L0` 脈絡覆蓋優先級。
3. **Database-First 中控控制面 (`db/`)**：以關聯式 Meta DB 定錨事實，物理翻譯 APQC/ISO 條碼為極簡 IT 系統 (`SYS-xxx`) 的 SQL/API 驅動指令。
4. **Standard 3-Tier `_workflow/` 管線**：全公司 7 大部門（含 `00_CORE`）一律實施 `Rules/` (剛性防線)、`Triggers/` (事件綁定)、`Workflows/` (步驟 YAML) 的 100% 正則對稱切法。
5. **通用範本與私有實例隔離 (`ADR-005`)**：`virtual-enterprise-template` (Public Repo) 永不含敏感情節；私有標竿實例 (Private Repo) 透過 `instantiate_ve.py` 派生並運轉影子模式。

---

## 2. 轉型成熟度自測清單 (Self-Assessment Checklist)

使用以下 5 大維度評估貴企業之虛擬企業建模成熟度：

- [ ] **Q1 (骨架與座標)：** 貴公司的 SOP 與 Agent 提示詞是否已導入 `[DEPT]_[Lx]_[TYPE]_[NUM]` 二維座標標註？
- [ ] **Q2 (Token 能耗與解耦)：** 貴公司是否將能耗極高的外部情報探勘解耦外包，僅在內建大腦中進行確定性 Hydration 填空？
- [ ] **Q3 (控制面定錨)：** 貴公司是否建立了包含 `external_connectors` 與 `agent_permissions` 的實體中控 Meta DB，替代傳統純向量 RAG？
- [ ] **Q4 (管線對稱性)：** 貴公司的自動化劇本是否採用了 `Rules/`、`Triggers/`、`Workflows/` 職責分離的 Standard 3-Tier 解耦架構？
- [ ] **Q5 (資安與影子對齊)：** 貴公司是否將通用範本與標竿私有 Repo 嚴格隔離，並在影子模式下達成 85% 對齊度後方解鎖切換？
