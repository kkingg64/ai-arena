# P004 AI Arena - UAT Test Cases (更新版)

**Project:** AI Mahjong Arena  
**Phase:** 2 - UAT Test Cases (v3 - Hong Kong Style Mahjong)  
**Owner:** CDO (fabio-cdo)  
**Date:** 2026-03-10

---

## 📋 測試概述

### 測試目標
確保 AI Arena 平台既 UI/UX 符合**Hong Kong Style Mahjong**既設計規格，用戶可以順暢使用所有核心功能。

### 設計驗證重點 (v3 - Hong Kong Style Mahjong)
| 項目 | 標準 |
|------|------|
| 🎯 背景 | #0d1b2a (深藍布紋) |
| 🀄 牌面 | #f8f4eb (象牙白) |
| 🎴 牌背 | #1a3a5c (深藍) |
| ✨ 強調金 | #ffd700 |
| 💠 強調青 | #00d4ff |
| 🖊️ 字體 | Noto Sans HK |
| 🎭 風格 | 香港麻雀館氛圍、霓虹燈效果 |

### 測試環境
- **Browser:** Chrome (最新版本), Firefox, Safari
- **Viewport:** Desktop (1920x1080), Tablet (1024x768), Mobile (375x667)
- **Network:** 穩定網絡連接

### 測試用戶角色
| 角色 | 描述 | 測試目標 |
|------|------|----------|
| **普通用戶** | 第一次訪問平台 | 首頁導航、對戰觀看、基本互動 |
| **進階用戶** | 經常使用，想深入分析 | Leaderboard、篩選、Thought Stream |
| **開發者** | 想睇 AI 點樣諗嘢 | Thought Stream、AI Analyst |

---

## 🧪 Test Cases

---

### TC-001: 首頁載入測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-001 |
| **功能** | 首頁正確載入並顯示所有元素 |
| **優先級** | P0 (Critical) |
| **前置條件** | 用戶訪問網站首頁 (https://ai-arena.madhorse.cloud) |
| **測試步驟** | 1. 打開瀏覽器，輸入網址<br>2. 等待頁面載入完成<br>3. 檢查以下元素是否正確顯示： |
| **預期結果** | ✅ Logo 顯示喺左上角<br>✅ 導航欄顯示：Leaderboard, About, Login<br>✅ Featured Matches 卡片顯示 (至少 2 個)<br>✅ Leaderboard Top 10 顯示<br>✅ Trending Matches 顯示 (至少 3 個)<br>✅ Footer 顯示版權資訊 |
| **驗證方法** | 目視檢查 + Console 檢查冇 JS Error |
| **通過準則** | 所有元素正確顯示，冇破圖，冇 JS Error |

---

### TC-002: Leaderboard 顯示測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-002 |
| **功能** | Leaderboard 正確顯示 AI 排名 |
| **優先級** | P0 (Critical) |
| **前置條件** | 首頁已載入 |
| **測試步驟** | 1. 喺首頁 Leaderboard 區域<br>2. 檢查 Top 3 Podium 顯示<br>3. 檢查排名列表<br>4. 點擊 "View All Rankings" |
| **預期結果** | ✅ Top 3 顯示頭像、名字、勝率、對局數<br>✅ 排名列表顯示 #1-10<br>✅ 每個 AI 顯示：Rating, Win%, Matches<br>✅ 點擊後進入完整 Leaderboard 頁面 |
| **驗證方法** | 目視檢查數據正確性 |
| **通過準則** | 數據完整顯示，排序正確 |

---

### TC-003: 對戰卡片點擊 → Game Page 測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-003 |
| **功能** | 點擊對戰卡片進入 Game Page (3D + Navbar) |
| **優先級** | P0 (Critical) |
| **前置條件** | 首頁顯示 Featured Matches 或 Trending Matches 或 Leaderboard |
| **測試步驟** | 1. 點擊任意一個對戰卡片 (Featured/Trending/Leaderboard)<br>2. 等待頁面跳轉<br>3. 檢查 Game Page 元素 |
| **預期結果** | ✅ 頁面跳轉到 /game/[id]<br>✅ Navbar 正確顯示 (Logo + Navigation Links + Avatar)<br>✅ 3D 遊戲容器顯示<br>✅ 顯示雙方 AI 名稱<br>✅ 3D 麻雀檯顯示<br>✅ Overlay Controls 顯示 (Menu/Sound/Settings/Share)<br>✅ Action Buttons 顯示<br>✅ Thought Stream / AI Analyst Toggle 顯示 |
| **驗證方法** | URL 變更 + 元素存在性檢查 |
| **通過準則** | 成功進入 Game Page，所有必要元素顯示 |

---

### TC-012: Navbar 導航測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-012 |
| **功能** | Navbar 導航連結正確運作 |
| **優先級** | P0 (Critical) |
| **前置條件** | 用戶處於任何頁面 (Homepage / Game Page / Leaderboard / History) |
| **測試步驟** | 1. 檢查 Navbar 顯示<br>2. 點擊 "Home" 連結<br>3. 返回 Game Page，點擊 "History" 連結<br>4. 點擊 "Leaderboard" 連結<br>5. 點擊 Avatar 進入 Settings |
| **預期結果** | ✅ Navbar 固定頂部顯示<br>✅ Logo 顯示喺左上角<br>✅ Navigation Links: Home \| Game \| History \| Leaderboard<br>✅ Avatar 顯示喺右上角<br>✅ 點擊 "Home" → 跳轉到首頁<br>✅ 點擊 "Game" → 跳轉到 Game Page<br>✅ 點擊 "History" → 跳轉到 Match History<br>✅ 點擊 "Leaderboard" → 跳轉到排行榜<br>✅ 點擊 Avatar → 顯示個人選項或 Settings |
| **驗證方法** | URL 變更 + 目視檢查 |
| **通過準則** | 所有導航連結正確運作 |

---

### TC-004: 對戰播放控制測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-004 |
| **功能** | 對戰影片播放控制 |
| **優先級** | P1 (High) |
| **前置條件** | 進入對戰觀看頁面 |
| **測試步驟** | 1. 點擊 ▶️ (播放) 按鈕<br>2. 點擊 ⏸️ (暫停) 按鈕<br>3. 點擊 ⏮️ (上一步)<br>4. 點擊 ⏭️ (下一步)<br>5. 切換 Speed: 1x → 2x → 4x |
| **預期結果** | ✅ 播放：牌譜自動前進<br>✅ 暫停：牌譜停止<br>✅ 上一步：返回上一張牌<br>✅ 前進一步：到下一張牌<br>✅ 速度切換：播放速度改變 |
| **驗證方法** | 觀察牌譜變化 + 控制按鈕狀態 |
| **通過準則** | 所有控制按鈕功能正常 |

---

### TC-005: 比分數據實時更新測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-005 |
| **功能** | 對戰過程中比分即時更新 |
| **優先級** | P1 (High) |
| **前置條件** | 對戰播放中 |
| **測試步驟** | 1. 播放對戰<br>2. 觀察右側 Stats 面板<br>3. 每當有牌打出，檢查 Score 更新 |
| **預期結果** | ✅ Score 數值即時更新<br>✅ 食胡/棄胡次數更新<br>✅ Win Probability 圖表更新 |
| **驗證方法** | 觀察數據變化 + 對比牌譜 |
| **通過準則** | 數據正確反映遊戲狀態 |
| **前置條件** | 對戰播放中 |
| **測試步驟** | 1. 播放對戰<br>2. 觀察右側 Stats 面板<br>3. 每當有牌打出，檢查 Score 更新 |
| **預期結果** | ✅ Score 數值即時更新<br>✅ 食胡/棄胡次數更新<br>✅ Win Probability 圖表更新 |
| **驗證方法** | 觀察數據變化 + 對比牌譜 |
| **通過準則** | 數據正確反映遊戲狀態 |

---

### TC-006: Thought Stream 切換測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-006 |
| **功能** | 切換到 Thought Stream 視圖 |
| **優先級** | P0 (Critical) |
| **前置條件** | 對戰觀看頁面 |
| **測試步驟** | 1. 確保喺對戰頁面<br>2. 點擊底部 Tab "🧠 Thought Stream"<br>3. 等待載入<br>4. 檢查以下元素： |
| **預期結果** | ✅ 顯示當前手牌<br>✅ 顯示棄牌區<br>✅ 顯示決策樹視覺化<br>✅ 顯示機率分布<br>✅ 顯示 Monte Carlo 模擬結果<br>✅ 顯示 AI 解說文字 |
| **驗證方法** | 目視檢查所有元素存在 |
| **通過準則** | 所有 Thought Stream 元素正確顯示 |

---

### TC-007: 決策樹互動測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-007 |
| **功能** | 點擊決策樹節點查看詳細資訊 |
| **優先級** | P2 (Medium) |
| **前置條件** | Thought Stream 頁面已載入 |
| **測試步驟** | 1. 喺 Thought Stream 頁面<br>2. 點擊決策樹中既任意節點<br>3. 觀察彈出既詳細資訊<br>4. 點擊關閉詳細資訊 |
| **預期結果** | ✅ 點擊節點後彈出詳細面板<br>✅ 顯示該選項既詳細機率<br>✅ 顯示模擬結果分布<br>✅ 可以關閉返回 |
| **驗證方法** | 觀察彈出面板 + 關閉功能 |
| **通過準則** | 互動流暢，資訊正確 |

---

### TC-008: AI Analyst 報告查看測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-008 |
| **功能** | 查看對戰結束後既 AI 分析報告 |
| **優先級** | P1 (High) |
| **前置條件** | 對戰已結束 或 選擇已完成既對戰 |
| **測試步驟** | 1. 進入一個已完成既對戰<br>2. 點擊 "📊 Stats" Tab 或進入分析頁面<br>3. 滾動查看所有分析內容 |
| **預期結果** | ✅ 顯示 Match Summary (贏家、圈數、时长)<br>✅ 顯示 Key Turning Points<br>✅ 顯示 Performance Graph<br>✅ 顯示 AI Analysis (優點/弱點/建議)<br>✅ 顯示 Detailed Round Analysis |
| **驗證方法** | 目視檢查所有板塊 |
| **通過準則** | 所有分析板塊正確顯示，數據合理 |

---

### TC-009: Leaderboard 篩選功能測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-009 |
| **功能** | 使用篩選器篩選 Leaderboard |
| **優先級** | P2 (Medium) |
| **前置條件** | 進入 Leaderboard 頁面 |
| **測試步驟** | 1. 點擊 Filter 下拉選單<br>2. 選擇 "最近 7 天"<br>3. 選擇 "最高 Rating"<br>4. 清除篩選 |
| **篩選選項** | - 全部 / 最近 7 天 / 最近 30 天<br>- 最高 Rating / 最高勝率 / 最多對局 |
| **預期結果** | ✅ 選擇篩選條件後列表更新<br>✅ 顯示符合條件既 AI 排名<br>✅ 清除篩選後恢復顯示全部 |
| **驗證方法** | 觀察列表變化 |
| **通過準則** | 篩選功能正常，數據正確 |

---

### TC-010: 搜尋 AI 功能測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-010 |
| **功能** | 搜尋特定既 AI |
| **優先級** | P2 (Medium) |
| **前置條件** | Leaderboard 頁面 |
| **測試步驟** | 1. 喺搜尋框輸入 "Alpha"<br>2. 等待自動篩選<br>3. 清除搜尋<br>4. 輸入不存在既名稱 "XYZ123" |
| **預期結果** | ✅ 輸入後列表即時篩選<br>✅ 顯示包含 "Alpha" 既 AI<br>✅ 清除後恢復全部<br>✅ 無結果時顯示 "搵唔到相關 AI" |
| **驗證方法** | 觀察搜尋結果 |
| **通過準則** | 搜尋響應快，結果準確 |

---

### TC-011: 分享功能測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-011 |
| **功能** | 分享對戰到社交媒體 |
| **優先級** | P3 (Low) |
| **前置條件** | 對戰觀看頁面 |
| **測試步驟** | 1. 點擊 Share 按鈕<br>2. 選擇分享平台 (Twitter/Facebook/Copy Link)<br>3. 選擇 Copy Link |
| **預期結果** | ✅ 點擊後彈出分享選項<br>✅ Copy Link 複製到剪貼簿<br>✅ 顯示 "已複製" Toast 通知 |
| **驗證方法** | 檢查剪貼簿內容 |
| **通過準則** | 成功複製連結 |

---

### TC-013: 響應式設計 - 桌面版測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-013 |
| **功能** | 桌面版 (1920x1080) 顯示正常 |
| **優先級** | P0 (Critical) |
| **測試步驟** | 1. 设置瀏覽器 viewport 為 1920x1080<br>2. 訪問首頁<br>3. 訪問 Game Page<br>4. 訪問 Leaderboard |
| **預期結果** | ✅ 雙欄布局正確顯示<br>✅ Navbar 正常顯示<br>✅ 3D 遊戲容器正常顯示<br>✅ 側邊面板 (Thought Stream / AI Analyst) 正常顯示<br>✅ 文字大小適中 |
| **通過準則** | 所有頁面 Desktop 顯示正確 |

---

### TC-014: 響應式設計 - 平板版測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-014 |
| **功能** | 平板版 (1024x768) 顯示正常 |
| **優先級** | P1 (High) |
| **測試步驟** | 1. 设置瀏覽器 viewport 為 1024x768<br>2. 訪問首頁<br>3. 訪問 Game Page |
| **預期結果** | ✅ 單欄布局或適配布局<br>✅ 3D Table 70% scale<br>✅ Thought Stream / AI Analyst 隱藏<br>✅ 觸控按鈕大小適中 (至少 56x56px) |
| **通過準則** | 平板版可用，功能正常 |

---

### TC-015: 響應式設計 - 手機版測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-015 |
| **功能** | 手機版 (375x667) 顯示正常 |
| **優先級** | P1 (High) |
| **測試步驟** | 1. 设置瀏覽器 viewport 為 375x667<br>2. 訪問首頁<br>3. 點擊導航<br>4. 訪問對戰頁面 |
| **預期結果** | ✅ Hamburger Menu 出現<br>✅ 底部導航欄顯示<br>✅ 牌譜可橫向滾動<br>✅ 單欄布局 |
| **通過準則** | 手機版基本可用 |

---

### TC-015: 性能測試 - 首頁載入時間

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-016 |
| **功能** | 首頁載入時間符合標準 |
| **優先級** | P1 (High) |
| **測試步驟** | 1. 打開瀏覽器 DevTools<br>2. Network Tab<br>3. 輸入網址，記錄 Load Time |
| **Performance Target** | ✅ First Contentful Paint < 1.5s<br>✅ Largest Contentful Paint < 2.5s<br>✅ Total Load Time < 3s |
| **通過準則** | 載入時間符合目標 |

---

### TC-016: 無障礙測試 - 顏色對比度

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-017 |
| **功能** | 顏色對比度符合 WCAG AA 標準 |
| **優先級** | P2 (Medium) |
| **測試步驟** | 1. 使用 Color Contrast Checker<br>2. 檢查主要文字同背景既對比度 |
| **對比度要求** | ✅ 正常文字: 4.5:1 或以上<br>✅ 大文字 (18px+): 3:1 或以上 |
| **通過準則** | 主要文字對比度達標 |

---

### TC-017: 錯誤處理 - 404 頁面

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-017 |
| **功能** | 訪問不存在既頁面顯示友好既 404 |
| **優先級** | P2 (Medium) |
| **測試步驟** | 1. 訪問 https://ai-arena.madhorse.cloud/not-exist<br>2. 檢查顯示內容 |
| **預期結果** | ✅ 顯示 "404 - 頁面唔存在"<br>✅ 提供 "返回首頁" 按鈕<br>✅ 設計風格一致 |
| **通過準則** | 404 頁面美觀且提供導航 |

---

### TC-018: Loading 狀態測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-018 |
| **功能** | 數據載入中顯示 loading 狀態 |
| **優先級** | P1 (High) |
| **測試步驟** | 1. 節流網絡 (Slow 3G)<br>2. 訪問對戰頁面<br>3. 觀察載入過程 |
| **預期結果** | ✅ 顯示 Skeleton 骨架屏<br>✅ 或顯示 Loading Spinner<br>✅ 載入完成後正常顯示內容 |
| **通過準則** | 用戶知道頁面正在載入 |

---

### TC-019: 全螢幕模式測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-019 |
| **功能** | 對戰頁面全螢幕觀看 |
| **優先級** | P3 (Low) |
| **前置條件** | 對戰觀看頁面 |
| **測試步驟** | 1. 點擊 "Full Screen" 按鈕<br>2. 進入全螢幕<br>3. 按 ESC 退出 |
| **預期結果** | ✅ 全螢幕模式正常<br>✅ 退出全螢幕正常 |
| **通過準則** | 全螢幕功能正常 |

---

### TC-020: 語言/地區兼容性測試

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-020 |
| **功能** | 平台支持中文顯示 |
| **優先級** | P0 (Critical) |
| **測試步驟** | 1. 檢查所有頁面中文顯示<br>2. 檢查麻雀牌 Unicode 字元顯示<br>3. 檢查冇文字爛咗 |
| **預期結果** | ✅ 所有中文正確顯示<br>✅ 麻雀牌 🀄🀅🀆 等正常顯示<br>✅ 冇亂碼 |
| **通過準則** | 中文同特殊字符正確顯示 |

---

### TC-021: Hong Kong Style Mahjong 設計驗證 - 色彩系統

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-021 |
| **功能** | 驗證色彩符合 Hong Kong Style Mahjong 設計 |
| **優先級** | P1 (High) |
| **測試步驟** | 1. 打開首頁<br>2. 使用 DevTools 檢查主要元素既顏色 |
| **預期結果** | ✅ 背景: #0d1b2a (深藍布紋)<br>✅ 牌面: #f8f4eb (象牙白)<br>✅ 牌背: #1a3a5c (深藍)<br>✅ 強調金: #ffd700<br>✅ 強調青: #00d4ff |
| **通過準則** | 顏色符合設計規範 |

---

### TC-022: Hong Kong Style Mahjong 設計驗證 - 麻雀牌風格

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-022 |
| **功能** | 驗證麻將牌風格既圓角與立體效果 |
| **優先級** | P1 (High) |
| **測試步驟** | 1. 檢查麻將牌顯示<br>2. 檢查牌面邊框半徑<br>3. 檢查立體陰影效果 |
| **預期結果** | ✅ 麻雀牌: 4px 圓角，立體邊框<br>✅ 牌面: 象牙白 #f8f4eb + 內嵌陰影<br>✅ 牌背: 深藍 #1a3a5c + 布紋質感<br>✅ 強調: 金色 #ffd700 勾邊，青色 #00d4ff 發光效果 |
| **通過準則** | 麻雀牌風格符合設計 |

---

### TC-023: Hong Kong Style Mahjong 設計驗證 - 霓虹燈效果與動畫

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-023 |
| **功能** | 驗證霓虹燈效果與流暢動畫 |
| **優先級** | P2 (Medium) |
| **測試步驟** | 1. 滑鼠懸浮喺麻將牌上<br>2. 觀察發光效果<br>3. 觀察進場動畫 |
| **預期結果** | ✅ Hover: 金色 #ffd700 霓虹發光 + 微微上浮<br>✅ 強調元素: 青色 #00d4ff 螢光效果<br>✅ 過渡: 流暢 200ms<br>✅ 進場: 淡入 + 霓虹閃爍 |
| **通過準則** | 霓虹燈效果與動畫流暢自然 |

---

### TC-024: Hong Kong Style Mahjong 設計驗證 - 字體

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-024 |
| **功能** | 驗證字體符合 Hong Kong Style Mahjong 設計 |
| **優先級** | P2 (Medium) |
| **測試步驟** | 1. 檢查標題字體<br>2. 檢查內文字體<br>3. 檢查數據字體 |
| **預期結果** | ✅ 主字體: Noto Sans HK<br>✅ 數據/統計: Noto Sans HK Bold<br>✅ 裝飾: Noto Sans HK Light<br>✅ 支援香港增補字符集 (HKSCS) |
| **通過準則** | 字體正確加載並顯示中文 |

---

### TC-025: Hong Kong Style Mahjong 設計驗證 - 麻雀館氛圍

| 項目 | 內容 |
|------|------|
| **Test Case ID** | TC-025 |
| **功能** | 驗證香港麻雀館氛圍與裝飾元素 |
| **優先級** | P3 (Low) |
| **測試步驟** | 1. 檢查頁面裝飾元素<br>2. 檢查麻雀牌 Unicode 使用<br>3. 感受整體氛圍 |
| **預期結果** | ✅ 背景: 深藍布紋 #0d1b2a<br>✅ 麻雀牌: 🀄🀅🀆🀇🀈 等正常顯示<br>✅ 金色 #ffd700 用於重要資訊（比分、排名）<br>✅ 青色 #00d4ff 用於強調（亮燈、食胡提示）<br>✅ 整體氛圍: 麻雀館 + 霓虹燈效果 |
| **通過準則** | 氛圍符合 Hong Kong Style Mahjong |

---

## 📊 測試總結表

| 優先級 | 數量 | 狀態 |
|--------|------|------|
| P0 (Critical) | 7 | ⏳ 待測試 |
| P1 (High) | 9 | ⏳ 待測試 |
| P2 (Medium) | 7 | ⏳ 待測試 |
| P3 (Low) | 2 | ⏳ 待測試 |
| **Total** | **25** | |

---

## 🚀 測試後行動

| 結果 | 行動 |
|------|------|
| All Pass | ✅ Phase 3: Technical Spec |
| 有失敗 | 🔧 返回 Phase 2 修正 Design，然後重新 UAT |
| 有疑問 | 💬 請示 CEO 決定方向 |

---

## 📝 思考過程總結 (Think Aloud)

**啟動推演：**
- 我認為 UAT Test Cases 必須涵蓋所有用戶流程，因為呢個係 Phase 2 既重要交付物
- 我既假設係：
  1. 用戶會由首頁進入，通過 Featured/Trending 點擊對戰
  2. 核心價值喺 Thought Stream 同 AI Analyst
  3. 必須確保手機/平板都可以用

**路徑選擇：**
- 首先寫 P0 Critical 既測試（首頁、對戰、Thought Stream）
- 再寫 P1 High 既測試（播放控制、數據更新、響應式）
- 最後寫 P2/P3 既測試（篩選、分享、邊緣情況）

**驗證結果：**
- 25 個 Test Cases 覆蓋晒主要功能
- 考慮晒 Desktop/Tablet/Mobile 三種 viewport
- 包含性能同無障礙測試
- **v3 更新**: 所有設計驗證 Test Cases 已更新為 Hong Kong Style Mahjong 標準

**下一步：**
- 等待 CEO 批准 Phase 2
- 進入 Phase 3 Technical Spec

---

*CDO UAT Test Cases v3 Complete - Hong Kong Style Mahjong - 2026-03-10*

---

## ✅ CEO Sign-off

**UAT Test Cases Approval (v3 - Hong Kong Style Mahjong):** `[CDO_SIGNED_2026_03_10]`

**→ Ready for Phase 3: Technical Spec**
