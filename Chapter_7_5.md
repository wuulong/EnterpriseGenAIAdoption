# 7.5 通用範本 (SSOT Vessel) 派生與私有標竿實例 (OSINT Hydration) 影子運轉 [v1.7.0]

## 1. 範本與實例的嚴格隔離原則 (`ADR-005`)

在企業級部署中，為保護商業機密並維持範本的純粹性，實施 **「通用範本與私有標竿實例嚴格隔離」** 戰略：

- **`virtual-enterprise-template` (Public Repo / SSOT Vessel)**：永遠保持純粹、通用、抽象之 L0-L4 骨架、APQC/ISO 控制點與 `book/00_toc.md` 意圖大綱。**嚴禁包含任何特定企業/診所之敏感個案、病患隱私或商業機密**。
- **`virtual-enterprise-[instance]` (Private Repo / Hydrated Instance)**：針對特定標竿企業（如在宅醫療診所）所開立之私有儲存庫（如 `virtual-enterprise-in-home-clinic`），專門承載 OSINT 收集之真實營運血肉與專屬表單。

---

## 2. 一鍵派生腳本 (`instantiate_ve.py`) 工序

為實現無摩擦派生，提供標準化工具腳本 [virtual-enterprise-template/scripts/instantiate_ve.py](file:///Users/wuulong/github/bmad-pa/events-2026Q3/virtual-enterprise/virtual-enterprise-template/scripts/instantiate_ve.py)：

```bash
# 發動一鍵派生指令
/usr/bin/python3 scripts/instantiate_ve.py \
  events-2026Q3/virtual-enterprise/virtual-enterprise-in-home-clinic \
  --name "在宅醫療診所" \
  --code "CLINIC" \
  --init-git
```

### 派生腳本物理作業：
1. 自動複製 `virtual-enterprise-template` 完整 L0-L4 骨架與 `_workflow/` 目錄（自動排除內層 `.git`）。
2. 自動建置新實例專屬之 `db/control_plane.sqlite` 資料庫。
3. 自動執行新目標目錄之獨立 `git init -b main`。

---

## 3. 影子模式 (Shadow Mode) 測試與 85% 對齊切換標誌

在 Private Repo 派生完成並注入 OSINT 血肉後，開啟 **影子模式 (Shadow Mode)**：

```mermaid
graph TD
    REAL["真實企業日常個案 (去識別化)"]
    SANDBOX["私有標竿虛擬企業沙盒 (Private Instance Repo)"]
    COMPARE["Gap Analysis 差異比對引擎"]
    CUTOVER["漸進式切換 (Cutover)\n(對齊度 >= 85%)"]

    REAL --> SANDBOX
    REAL --> COMPARE
    SANDBOX --> COMPARE
    COMPARE -->|對齊度 >= 85%| CUTOVER
```

1. **資料雙送**：將去識別化之真實個案同步抄送給真實員工與 Agent 網路。
2. **Gap Analysis**：比對兩者產出之差異與合規性。
3. **85% 閥值解鎖**：當對齊度達到 85% 以上時，正式解鎖從「人機對合 (Human-in-the-loop)」切換至「例外管理 (Management by Exception)」的自動化營運。
