import os
import re

# 定義台灣語感校準映射表 (針對企業賦能專案進行優化)
# 格式: { "錯誤詞彙": "建議修正詞彙" }
LINGUISTIC_MAPPING = {
    "代碼": "程式碼",
    "數據": "資料",
    "項目": "專案",
    "運行": "運作",
    "產出式": "生成式",
    "生成式": "生成式", # 保留生成式
    "生成": "產出", # 其他場合轉產出
    "信息": "訊息",
    "大通稿": "完整匯整檔",
    "激活": "啟動",
    "軟件": "軟體",
    "硬件": "硬體",
    "硬盤": "硬碟",
    "內存": "記憶體",
    "設置": "設定",
    "對標": "對位",
    "武裝": "裝備",
    "網絡": "網路",
    "屏幕": "螢幕",
    "設備": "裝置",
    "脫敏": "去識別化",
    "優化": "最佳化",
    "實際情況": "實際",
    "個性化": "個人化",
    "渠道": "管道",
    "菜單": "選單",
    "視頻": "影片",
    "音頻": "音訊",
    "用戶": "使用者",
    "支持": "支援",
    "文件": "檔案",
    "流程": "程序",
    "程序": "程序", # 保留程序
}

def align_content(content):
    """
    對內容進行校準。採用正則表達式單次掃描，確保長詞優先，且不被後續短詞誤傷。
    """
    # 建立正則表達式，按長度倒序排列
    pattern = re.compile("|".join(re.escape(key) for key in sorted(LINGUISTIC_MAPPING.keys(), key=len, reverse=True)))
    
    # 使用正則表達式切分代碼塊與非代碼塊
    parts = re.split(r'(```[\s\S]*?```)', content)
    
    new_parts = []
    for part in parts:
        if part.startswith('```'):
            if part.startswith('```mermaid'):
                # Mermaid 圖表執行校準
                new_parts.append(pattern.sub(lambda m: LINGUISTIC_MAPPING[m.group(0)], part))
            else:
                # 其他代碼塊保持原樣
                new_parts.append(part)
        else:
            # 非代碼區執行校準
            new_parts.append(pattern.sub(lambda m: LINGUISTIC_MAPPING[m.group(0)], part))
            
    return "".join(new_parts)

def process_directory(target_dir):
    print(f"🚀 開始企業賦能全書語感校準 (v2: 單次掃描模式)...")
    print(f"目標目錄: {target_dir}")
    
    files_processed = 0
    
    for root, dirs, files in os.walk(target_dir):
        # 排除 git 目錄
        if '.git' in dirs:
            dirs.remove('.git')
            
        for filename in files:
            # 排除特定檔案，僅處理 Markdown
            if filename.endswith(".md") and filename not in ["LICENSE"]:
                file_path = os.path.join(root, filename)
                
                with open(file_path, "r", encoding="utf-8") as f:
                    original_content = f.read()
                
                new_content = align_content(original_content)
                
                if new_content != original_content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"  [FIXED] {os.path.relpath(file_path, target_dir)}")
                    files_processed += 1
    
    print(f"\n✅ 校準完成！")
    print(f"共處理檔案數: {files_processed}")

if __name__ == "__main__":
    # 設定目標目錄為工作區根目錄
    # 腳本路徑: [Root]/EnterpriseGenAIAdoption/scripts/align_taiwanese_linguistics.py
    SCRIPT_PATH = os.path.abspath(__file__)
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_PATH)))
    process_directory(ROOT_PATH)
