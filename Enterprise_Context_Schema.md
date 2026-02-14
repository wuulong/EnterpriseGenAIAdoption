---
title: 企業 AI 轉型先行診斷書
version: v1.3.0
compatible_book_range: ["v1.3.x"]
type: Diagnostic Schema
---
# 📋 企業 AI 轉型先行診斷書 (Enterprise Context Schema) [v1.3.0]
**診斷邏輯**：採「感官偵測 (五大維度) -> 實體封裝 (L0-L4)」之對應流程。

---

## 一、 感官偵測 (Detection): 五大維度問診
透過以下五個切角觀察企業現狀，得分將映射至 L0-L4 的參數權重。

1.  **容錯成本與合規深度** (映射至 L1):
    *   [ ] 嚴謹合規 (Low Tolerance) <---> [ ] 開放創意 (High Tolerance)
2.  **資料資產熵值與流動性** (映射至 L3):
    *   [ ] 紙本/遺留系統 (Legacy) <---> [ ] 數位原生/API (Native)
3.  **業務工作同質化程度** (映射至 L2):
    *   [ ] 破碎例外處理 <---> [ ] 高度 SOP 化
4.  **決策敏捷度與市場窗口** (映射至 L0):
    *   [ ] 傳統層級制 (Slow) <---> [ ] 敏捷決策 (Fast)
5.  **轉型信仰度與先行者密度** (映射至 L4):
    *   [ ] 管理者意志缺乏 <---> [ ] 具備五星特質之 Wing Group 成員

---

## 二、 脈絡封裝 (Packaging): L0-L4 實體整備度
根據第一階段問診，評估各層級脈絡檔案的建檔難度與需求。

### L0: 工作型態層 (Work Style)
*   **溝通協議**： [ ] 同步會議導向 [ ] 非同步 Task-based
*   **工具鏈整備**： [ ] 碎片化通訊 [ ] 具備統一任務管理平台

### L1: 產業領域層 (Domain)
*   **法規約束**： [ ] 無特殊限制 [ ] 具備嚴格產業規範 (如 HIPAA, GDPR)
*   **特定術語集需求**：是否需建立專屬產業詞典？

### L2: 職能邏輯層 (Logic)
*   **口袋技能 (Pocket Skills) 掃描**：一線員工是否已有非官方的 AI 使用習慣？
*   **任務拆解能力**：現有 SOP 是否具備可程式化邏輯？

### L3: 企業實體層 (Entity)
*   **核心資產 Markdown 化等級**： [ ] 0% [ ] 50% [ ] 100%
*   **私有資料字典**：是否已建立公司內部的專有名詞對照表？

### L4: 個人特質層 (Sovereignty)
*   **主權意識**：員工是否渴望奪回被重複勞動佔據的時間？
*   **數位分身 (Decision History) 整備**：是否具備能代表個人決策風格的歷史對話/文件？

---

## 三、 組織對合度 (Synthesis Alignment)
*   **三明治轉型熱度**：
    *   Top-down 推力 (CoE 支持度): [1-10]
    *   Bottom-up 拉力 (先行者熱情): [1-10]
*   **首戰案例 (Pilot) 選擇**：應選擇 L4/L2 整合度最高的場景切入。

---

## 四、 技術對合協議 (Technical Protocol): Session Manifest Spec
[v1.3.0 實體化關鍵] 當診斷完成後，應根據具體任務生成「羅盤對合」後的掛載協議：

```yaml
session_id: "UID_SESSION_GENERIC"
# 層次化脈絡實體路徑 (Lx Vessel Mapping)
layers:
  L0_Workstyle: "frameworks/L0_Base_[Style].md"
  L1_Domain: "frameworks/L1_Domain_[Industry].md"
  L2_Function: "frameworks/L2_Func_[Role]_T_Pattern.md"
  L3_Entity: "frameworks/L3_Entity_[Company].md"
  L4_Sovereignty: "sandbox/L4_User_[Name]_Vibe.md"

# 羅盤參數對合 (Compass Alignment Logic)
stacking_logic:
  priority: "L4 > L3 > L2 > L1 > L0" # 預設堆疊優先序
  constraints:
    L1_Hard_Filter: true  # 是否啟動產業法規硬過濾 (如底端象限)
    L4_Overlay_Style: true # 是否允許個人風格覆蓋 (如頂端象限)
```

---

## ✅ 診斷結論與映射建議
*   **建議定位**：(參考 2D 矩陣座標)
*   **脈絡載體掛載序位**：(優先處理層級，如：L1-First 或 L4-First)
*   **Manifest 生成狀態**：[ ] 未生成 [ ] 已產出範本 [ ] 已動態聯集
