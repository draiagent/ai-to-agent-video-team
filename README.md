# AI to Agent 智慧製片團隊

**ai-to-agent-video-team**｜以角色分工、鏡頭工作圖卡與驗收流程，將影片製作整理成可交接給 Agent 的任務。

![版本](https://img.shields.io/badge/version-0.1.0-blue)

![益力康陳董小秘書介紹](assets/images/01-introduction.png)

## 為什麼需要這個專案

對象是講師、內容創作者與企業行銷團隊。解決素材各自漂亮，卻缺少故事、連續性、節奏與交付規格的問題。

## 範圍與狀態

目前為 **0.1.0 方法論與教學教材**（已發布為公開 Repo，tag v0.1.0），包含 8 張圖卡、網誌文章、八步流程、工具對照、Agent 任務指令、工作圖卡模板與教學案例。

本專案沒有 API 串接、自動生成影片的執行程式或可安裝 Skill/MCP；不得將文件範例宣稱為已完成的影片實測。授權為保留所有權利（All rights reserved）；已建立公開 Repo 與 tag v0.1.0，尚未建立 GitHub Release。

## 如何運作

- 九項製作工序：腳本 → 角色 → 配音 → 圖片 → 動態 → 剪輯 → 配樂 → 音效 → 調色。
- 八步專案流程：定義任務 → 腳本分鏡 → 視覺與聲音 → 節奏預覽 → 動態鏡頭 → 剪輯與聲音 → 調色驗收 → 交付保存。
- 人保留三項判斷：**劇情方向、情緒價值、符合形象**。
- 輸入：主題、受眾、片長、比例、品牌素材、參考風格、預算與權限。
- 輸出：分鏡、逐鏡工作圖卡、素材清單、影片各版本與驗收紀錄；本 Repo 提供其規格，非已生成的成片。
- 驗收：檔案可開啟、內容符合任務、聲畫與角色一致、成本有紀錄、人工判斷完成。

## 快速開始

不需安裝製片程式。先閱讀 [網誌文章](docs/blog.md)，再依序：

1. 閱讀 [八步流程](docs/workflow.md) 與 [工具分工](docs/tools.md)。
2. 複製 [鏡頭工作圖卡模板](docs/shot-task-card.md)，填入自己的需求。
3. 將 [Agent 任務指令](docs/agent-instructions.md) 與填好的圖卡交給可使用所需工具的 Agent。
4. 用 [30 秒影片教學案例](examples/30-second-video.md) 練習；先完成靜態分鏡與試配音，再生成動態。
5. 依 [驗收表](docs/acceptance.md) 檢查並留下證據。

具體練習輸入：「製作 30 秒、9:16 的 AI 課程介紹，繁體中文字幕，使用已授權品牌素材，先交付分鏡預覽。」預期先得到六個鏡頭的規格與預覽；工具未接通時應回報缺項，不得宣稱已生成。

## 適用場景

- AI 課程、製片任務設計與企業行銷協作。
- 建立製片 Agent 前的需求與驗收規格。
- 不適合作為已串接的全自動製片軟體或工具版本採購依據。

## 八張圖卡

| 頁碼 | 圖卡 |
|---|---|
| 01 | [你的 AI 製片團隊](assets/images/01-introduction.png) |
| 02 | [AI 影片製作全貌](assets/images/02-production-overview.png) |
| 03 | [AI 製片工具分工](assets/images/03-tools.png) |
| 04 | [影片製作 Agent：八步任務流程](assets/images/04-agent-workflow.png) |
| 05 | [一個鏡頭，一張工作圖卡](assets/images/05-shot-task-card.png) |
| 06 | [先預覽，再生成](assets/images/06-quality-and-cost.png) |
| 07 | [人與 Agent 協作](assets/images/07-collaboration-and-delivery.png) |
| 08 | [陳董總結：三個最有價值的判斷](assets/images/08-directors-judgment.png) |

## 檔案導覽

- `docs/`：文章、方法、工具、任務指令、模板與驗收表。
- `examples/`：完整填寫的教學案例，非實測影片。
- `assets/images/`：最新 8 張圖卡原始 PNG。
- `scripts/validate.py`：僅檢查發布包檔案、相對連結與圖片雜湊，非製片程式。
- `release/`：發布說明、檢查紀錄及圖卡雜湊清單。
- [CHANGELOG](CHANGELOG.md)、[貢獻規範](CONTRIBUTING.md)、[素材來源](ATTRIBUTION.md)。

## 版本與後續計畫

版本 0.1.0；日期 2026-10-25；文件可由 Markdown 閱讀器或 GitHub 顯示。

後續計畫：驗證工具接入、完成一次端到端影片實測。以上均未包含在本版完成項目中。

## 授權與署名

本 repo 採保留所有權利（All rights reserved），見 [LICENSE](LICENSE)，不是 MIT 或 CC 等開放授權；法律權利人為 AI Coach 益力康陳董。Logo、人物、玩偶與第三方品牌的使用範圍須獨立確認，詳見 [素材來源](ATTRIBUTION.md)。

AI Coach 益力康陳董 x CGM Coach 血糖教練 | 2026 AI to Agent | 2027 AI to AGI Agent

## 發布檢查紀錄

見 [驗證紀錄](release/VALIDATION.md)。首張圖卡尺寸與其餘七張有 1–2 像素差異；頁碼字級與座標的像素級一致性未驗證。
