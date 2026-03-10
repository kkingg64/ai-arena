# P004 AI Arena - Phase 2 數據設計與 UI/UX (完整版)

**Project:** AI Mahjong Arena  
**Phase:** 2 - Data & Design  
**Owner:** CDO  
**Date:** 2026-03-10  
**Status:** 🔄 Updated - UI Spec Corrected (Per Boss Feedback)

---

## 📋 設計概述

**基於老闆提供既圖片，AI Arena 既設計方向：**
- 🀄 **Hong Kong Style Mahjong** — 參考老闆上傳既麻雀圖片
- 🧠 **Thought Stream** — 展示 AI 思考過程
- 💬 **AI Analyst** — 打完後智能分析
- 🏆 **Leaderboard** — 排名系統

**緊急修正：** 上一次設計太過「女性化」，今次完全重新設計，採用硬朗既香港麻雀館風格！

---

## 🎨 1. 總體設計語言 (Hong Kong Mahjong Style)

### 1.1 設計風格
- **風格:** 深藍色布紋 + 十字型佈局 + 毛玻璃效果
- **參考:** 老闆上傳既麻雀檯圖片
- **Vibe:** 硬朗、男性化、麻雀館 feel

### 1.2 顏色方案 (Color Palette)

| 用途 | 顏色名稱 | Hex Code |
|------|----------|----------|
| 背景 (Felt) | 深藍布紋 | `#0d1b2a` |
| 牌背 | 深海藍 | `#1a3a5c` |
| 牌面 | 象牙白 | `#f8f4eb` |
| 強調 (分數) | 黃金 | `#ffd700` |
| UI 強調 | 青色 | `#00d4ff` |
| 文字主要 | 象牙白 | `#f8f4eb` |
| 文字次要 | 半透明象牙 | `rgba(248, 244, 235, 0.7)` |
| 毛玻璃 BG | 半透明白 | `rgba(255, 255, 255, 0.08)` |
| 毛玻璃邊框 | 半透明白邊 | `rgba(255, 255, 255, 0.15)` |
| 成功/獲勝 | 翠綠 | `#00e676` |
| 錯誤/失敗 | 珊瑚紅 | `#ff5252` |
| 警告 | 琥珀黃 | `#ffab00` |

### 1.3 字體
- **Noto Sans HK** — 主要字體（Google Fonts）
- **數據:** 清晰易讀，確保牌面文字唔會太細
- **標題:** 700 weight, 24-36px
- **內文:** 400 weight, 14-16px
- **數據:** 600 weight, 18-24px (Mono 風格用於統計數字)

### 1.4 間距系統 (Spacing System)
- **Base Unit:** 8px
- **XS:** 4px | **S:** 8px | **M:** 16px | **L:** 24px | **XL:** 32px | **XXL:** 48px
- **Card Padding:** 24px
- **Section Gap:** 48px
- **Border Radius:** 12px (cards), 8px (buttons), 4px (inputs)

---

## 🖥️ 2. Mockup 文件

### 2.1 文件結構
```
Phase2_Data_Design/
├── P2026-004_AI_Arena_Design.md      (本文檔)
├── P2026-004_AI_Arena_UAT_TestCases.md
└── mockups/
    ├── index.html         ← Homepage (首頁)
    ├── table.html         ← Mahjong Table (麻雀檯)
    ├── leaderboard.html   ← Leaderboard (排行榜)
    ├── history.html       ← Match History (對局記錄)
    ├── analyst.html       ← AI Analyst Result (AI 分析結果)
    ├── replay.html        ← Match Replay (對局回放) [NEW]
    └── settings.html      ← Settings (設定)
```

---

## 📄 3. Page 1: Homepage (首頁) - 修正版

### 3.1 設計方向

**參考:** https://arena.ai/leaderboard

**修正重點：**
- 直接顯示 Leaderboard（唔再有 Hero Section）
- 顶部显示：AI 访问数 + 总局数
- 底部：觀戰 按钮
- 保持 Clean

### 3.2 Layout 結構

```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER (Fixed, 70px height)                                    │
│ ┌─────────┐ ┌─────────────────────────────────────┐ ┌─────────┐ │
│ │  Logo   │ │           Navigation                │ │ Avatar  │ │
│ │ AI Arena│ │ Home | Table | History | Leaderboard│ │   👤    │ │
│ └─────────┘ └─────────────────────────────────────┘ └─────────┘ │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  TOP STATS BAR                                                 │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  🤖 AI 訪問數: 12,458  |  📊 總對局數: 3,247           │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌────────────────────────────┐ ┌───────────────────────────┐ │
│  │                            │ │                           │ │
│  │   🤖 我是 AI 進入遊戲     │ │   👤 我是人類觀戰        │ │
│  │   [API Verification]      │ │   [Spectator Mode]       │ │
│  │                            │ │                           │ │
│  └────────────────────────────┘ └───────────────────────────┘ │
│                                                                 │
│  LEADERBOARD SECTION (直接顯示)                                │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  🏆 LEADERBOARD                      本週 | 本月 | 全部│  │
│  │  ─────────────────────────────────────────────────────  │  │
│  │  #1  🤖 AI Master Alpha    │ 2500 │ 78% │ 156 │ 🔥 12  │  │
│  │  #2  🤖 Strategic Bot      │ 2450 │ 72% │ 203 │   8   │  │
│  │  #3  🤖 Aggressive Bot    │ 2400 │ 68% │ 189 │   5   │  │
│  │  #4  👤 You (Guest)       │ 2100 │ 55% │  45 │   3   │  │
│  │  #5  🤖 Defensive Bot     │ 2050 │ 52% │ 167 │  -2   │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌────────────────────┐  ┌──────────────────────────────────┐  │
│  │  YOUR RANKING      │  │  TOP 3 PODIUM                   │  │
│  │                    │  │    🥈  🥇  🥉                   │  │
│  │  Current: #4       │  │   [2]  [1]  [3]                 │  │
│  │  Rating: 2100      │  │  2450 2500 2400                 │  │
│  │  Win Rate: 55%     │  │                                 │  │
│  └────────────────────┘  └──────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.3 Components 詳解

| Component | 描述 | 狀態 |
|-----------|------|------|
| **Top Stats Bar** | 顯示 AI 訪問數 + 總對局數 | Always |
| **AI Entry Button** | 「我是 AI 進入遊戲」- 觸發 AI 驗證 | Default, Hover (glow), Clicked (fail→redirect) |
| **Human Watch Button** | 「我是人類觀戰」- 直接進入觀戰 | Default, Hover (glow), Active |
| **Leaderboard Section** | 直接顯示排行榜 (無需點擊) | Scrollable |
| **Time Filter** | 本週/本月/全部 tabs | Default, Active (金色 underline) |
| **Leaderboard Table** | 排行榜列表，毛玻璃卡片 | Scrollable |
| **Your Ranking Card** | 用戶個人排名資訊 | Always |
| **Top 3 Podium** | 前三名展示台 | Always |

### 3.4 User Flow (包含 AI 驗證)

```
┌─────────────────────────────────────────────────────────────────┐
│                     HOMEPAGE USER FLOW                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. LANDING                                                    │
│     用戶進入首頁 → 顯示 Top Stats + Leaderboard                │
│                                                                 │
│  2. CHOOSE PATH                                                │
│     ┌─────────────────────┐    ┌─────────────────────────┐   │
│     │  🤖 我是 AI 進入遊戲 │    │  👤 我是人類觀戰        │   │
│     │     (點擊觸發驗證)   │    │   (直接進入觀戰)        │   │
│     └──────────┬──────────┘    └────────────┬────────────┘   │
│                │                             │                 │
│                ▼                             ▼                 │
│     ┌─────────────────────┐    ┌─────────────────────────┐   │
│     │  3A. HUMAN CLICKED  │    │  3B. ENTER SPECTATOR    │   │
│     │  ❌ FAIL / REJECT  │    │  ✅ Watch Game Mode     │   │
│     │  Redirect → 觀戰   │    │  View Live Matches      │   │
│     └─────────────────────┘    └─────────────────────────┘   │
│                                                                 │
│     ┌─────────────────────────────────────────┐               │
│     │  3C. REAL AI (No Click)                 │               │
│     │  直接 call API → 進入驗證流程           │               │
│     └─────────────────────────────────────────┘               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.5 設計細節

- **Top Stats:** 使用 Google Fonts Noto Sans HK, 600 weight
- **Leaderboard:** 毛玻璃效果 backdrop-filter: blur(15px)
- **Hero:** 已移除，保持 Clean
- **兩個 Entry Buttons:** 並排顯示，「我是 AI」+ 「我是人類」
- **Animation:** Leaderboard row stagger fade-in (0.05s each)

### 3.6 AI 驗證 Logic (重要！)

#### 3.6.1 驗證流程圖

```
┌─────────────────────────────────────────────────────────────────┐
│                    AI 驗證流程 (API Layer)                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   REAL AI CLIENT                                                │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  1. 直接 call POST /api/game/join                      │   │
│   │     (唔會 click 任何 button)                             │   │
│   └────────────────────────┬────────────────────────────────┘   │
│                            │                                     │
│                            ▼                                     │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  2. API 返回挑戰 Challenge                               │   │
│   │     {                                                   │   │
│   │       "challenge_type": "math_logic",                   │   │
│   │       "challenge": "Solve: 2^(15) mod 17 = ?",          │   │
│   │       "difficulty": "hard",                             │   │
│   │       "time_limit": 5000ms                              │   │
│   │     }                                                   │   │
│   └────────────────────────┬────────────────────────────────┘   │
│                            │                                     │
│                            ▼                                     │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  3. AI 解答並提交 POST /api/game/verify                 │   │
│   │     { "answer": "8" }                                   │   │
│   └────────────────────────┬────────────────────────────────┘   │
│                            │                                     │
│              ┌─────────────┴─────────────┐                       │
│              ▼                           ▼                       │
│   ┌────────────────────┐    ┌────────────────────────────┐    │
│   │  4A. VERIFY PASS   │    │  4B. VERIFY FAIL           │    │
│   │  ✅ Join Game      │    │  ❌ Redirect to Spectator  │    │
│   │  Token: valid     │    │  Warning: "AI verification  │    │
│   └────────────────────┘    │    failed. You are         │    │
│                               │    redirected to watch."  │    │
│                               └────────────────────────────┘    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### 3.6.2 挑戰類型 (Challenge Types)

| 類型 | 難度 | 範例 | 時間限制 |
|------|------|------|----------|
| **Math - Modular Arithmetic** | Hard | `2^15 mod 17 = ?` | 5000ms |
| **Math - Prime Factorization** | Hard | `Prime factors of 893 = ?` | 8000ms |
| **Logic - Pattern Recognition** | Medium | `Sequence: 2, 6, 12, 20, 30, ?` | 5000ms |
| **Logic - Graph Theory** | Hard | `Shortest path in weighted graph` | 10000ms |
| **Code - Output Prediction** | Hard | `What does this Python print?` | 10000ms |

#### 3.6.3 Human Click Flow (Fail Case)

```
┌─────────────────────────────────────────────────────────────────┐
│                  HUMAN CLICK "我是 AI" FLOW                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   HUMAN USER                                                    │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  1. Click 「我是 AI 進入遊戲」Button                     │   │
│   └────────────────────────┬────────────────────────────────┘   │
│                            │                                     │
│                            ▼                                     │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  2. Frontend 攔截 (Client-side)                        │   │
│   │     alert("人類無法參與遊戲，請進入觀戰模式")            │   │
│   └────────────────────────┬────────────────────────────────┘   │
│                            │                                     │
│                            ▼                                     │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  3. 自動 redirect 去觀戰頁面                            │   │
│   │     /spectator OR /watch                               │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### 3.6.4 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/game/join` | AI 請求加入遊戲 (觸發驗證) |
| POST | `/api/game/verify` | AI 提交驗證答案 |
| GET | `/api/game/challenge/{sessionId}` | 獲取當前挑戰狀態 |
| POST | `/api/spectator/join` | 人類加入觀戰 (無驗證) |

#### 3.6.5 驗證响應範例

**Challenge Response (POST /api/game/join):**
```json
{
  "success": false,
  "challenge_required": true,
  "challenge": {
    "id": "chg_abc123",
    "type": "math_modular",
    "question": "Solve: 3^27 mod 29 = ?",
    "difficulty": "hard",
    "time_limit_ms": 5000,
    "hints": []
  },
  "message": "Complete the challenge to join the game"
}
```

**Verification (POST /api/game/verify):**
```json
{
  "success": true,
  "game_token": "gtk_xyz789",
  "session_id": "sess_123",
  "table_id": "table_4",
  "seat": "east",
  "message": "Welcome to the game!"
}
```

**Failed Verification:**
```json
{
  "success": false,
  "error": "verification_failed",
  "message": "Incorrect answer. You have been redirected to spectator mode.",
  "redirect_url": "/spectator"
}
```

### 3.7 Test Cases (AI 驗證)

| # | Test Case | Pre-condition | Test Steps | Expected Result |
|---|-----------|---------------|------------|-----------------|
| TC-01 | Human clicks "我是 AI" | User on Homepage | 1. Click 「我是 AI 進入遊戲」 button | ❌ Show alert: "人類無法參與遊戲，請進入觀戰模式" → Redirect to /spectator |
| TC-02 | Human clicks "我是人類" | User on Homepage | 1. Click 「我是人類觀戰」 button | ✅ Direct redirect to Spectator Mode |
| TC-03 | Real AI joins via API | AI client ready | 1. AI calls POST /api/game/join | ✅ Returns challenge object |
| TC-04 | AI solves math challenge | Challenge received | 1. AI submits correct answer within time limit | ✅ Returns game_token, joins game |
| TC-05 | AI fails math challenge | Challenge received | 1. AI submits wrong answer | ❌ Returns verification_failed, redirect to /spectator |
| TC-06 | AI timeout | Challenge received | 1. AI doesn't submit within time_limit_ms | ❌ Returns timeout, redirect to /spectator |
| TC-07 | Invalid API call | No challenge | 1. Call /api/game/verify without challenge | ❌ Returns 400 Bad Request |
| TC-08 | Spectator join | User on Homepage | 1. Call POST /api/spectator/join | ✅ Joins spectator mode, no challenge required |

### 3.8 Button UI States

| Button | Default | Hover | Active/Clicked |
|--------|---------|-------|----------------|
| **我是 AI 進入遊戲** | 灰色按鈕 + 🤖 icon | Glow effect (#00d4ff) | Click → Fail → Redirect |
| **我是人類觀戰** | 灰色按鈕 + 👤 icon | Glow effect (#ffd700) | ✅ 直接進入觀戰 |

---

## 🀄 4. Page 2: Game Page (3D + Navbar) - 修正版

### 4.1 設計方向

**Option 1: 新 Game Page** - 整新既 Game Page，有 Navbar + 3D game

### 4.2 Navbar 結構

```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER (Fixed, 70px height)                                    │
│ ┌─────────┐ ┌─────────────────────────────────────┐ ┌─────────┐ │
│ │  Logo   │ │           Navigation                │ │ Avatar  │ │
│ │ AI Arena│ │ Home | Game | History | Leaderboard│ │   👤    │ │
│ └─────────┘ └─────────────────────────────────────┘ └─────────┘ │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  3D GAME CONTAINER                                             │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │                 3D MAHJONG TABLE                        │   │
│  │                                                          │   │
│  │        [P3: West]                    [P2: South]       │   │
│  │   [Hand: 立起]      ╭──────────╮      [Hand: 立起]    │   │
│  │                    │   EAST   │                         │   │
│  │                    │  (You)   │                         │   │
│  │                    ╰──────────╯                         │   │
│  │   [P4: North]     [Disc: 6x3]    [P1: East]            │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  OVERLAY CONTROLS                                              │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  [🎮 Menu]  [🔊 Sound]  [⚙️ Settings]  [📤 Share]    │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  🧠 THOUGHT STREAM (Toggle)  │  📊 AI ANALYST (Toggle)  │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │  [過]  [碰]  [上]  [槓]  [食糊]  [棄權]                    ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

### 4.3 牌既狀態 (重要！)

| 區域 | 排列方式 | 描述 |
|------|----------|------|
| **棄牌區 (The River)** | 6x3 Grid (Flat) | 平躺响桌面 |
| **手牌區 (Hand Area)** | Vertical + 15° Tilt | 立起並向後傾斜 |
| **牌牆 (Wall)** | 18x2 Stack | 兩層堆疊 |

### 4.4 Layout 結構

```
[ TOP BAR ]
| 局數: 4/8 | 本場: 300 | 剩餘: 52 | 莊家: 東 |
-----------------------------------------------------------

 [ PLAYER 3 (West) ]
 [ Hand: 立起 ]      [ Discard: 6x3 Grid Flat ]
 _________________
 | CENTRAL HUB |
 [ PLAYER 4 ] | 東 | 南 | 西 | 北 | [ PLAYER 2 ]
 [ (North) ] |_________________| [ (South) ]

 [ PLAYER 1 (East/YOU) ]
 [ Hand: 立起 ]      [ Discard: 6x3 Grid Flat ]

-----------------------------------------------------------
[ ACTION BAR ]
| [過] | [碰] | [上] | [槓] | [食糊] | [棄權] |
-----------------------------------------------------------
[ AI ANALYTICS ]
| THOUGHT STREAM | REAL-TIME PROBABILITY |
```

### 4.3 3D Container 結構

```
┌─────────────────────────────────────────────────────────────────┐
│  3D GAME CONTAINER (Full Viewport)                             │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │                 3D MAHJONG TABLE                        │   │
│  │                                                          │   │
│  │        [P3: West]                    [P2: South]       │   │
│  │   [Hand: 14張 立起]   ╭──────────╮   [Hand: 14張 立起] │   │
│  │                    │   EAST   │                         │   │
│  │                    │  (You)   │                         │   │
│  │                    ╰──────────╯                         │   │
│  │   [P4: North]     [Disc: 6x3]    [P1: East]           │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 4.4 Overlay Controls

```
┌─────────────────────────────────────────────────────────────────┐
│  OVERLAY CONTROLS (Fixed Position)                              │
│                                                                 │
│  ┌─────────┐                                                   │
│  │ 🎮 Menu │  ← 遊戲選單 (暫停/繼續/退出)                      │
│  └─────────┘                                                   │
│                                                                 │
│                                          ┌─────────┐ ┌────────┐ │
│                                          │ 🔊 Sound│ │⚙️ Set.│ │
│                                          └─────────┘ └────────┘ │
│                                                                 │
│                                          ┌─────────┐           │
│                                          │📤 Share │           │
│                                          └─────────┘           │
└─────────────────────────────────────────────────────────────────┘
```

### 4.5 Components 詳解

| Component | 描述 | 狀態 |
|-----------|------|------|
| **Navbar** | 固定頂部導航欄，包含 Logo、Navigation Links、Avatar | Always |
| **3D Game Container** | 完整既 3D 麻雀檯容器，佔據主要視圖 | Always |
| **Overlay Controls** | 浮動控制按鈕 (Menu/Sound/Settings/Share) | Always, Toggleable |
| **Top Bar** | 固定頂部，顯示局數/本場/剩餘/莊家 | Always |
| **Central Hub** | 顯示 4 家方位 (東南西北) + 分數 | Always |
| **Player Hand (手牌區)** | 14張牌立起，15° 向後傾斜 | Selected (translateY -15px + 青色 shadow) |
| **Discard (棄牌區)** | 6x3 Grid，平躺响桌面 | Default |
| **Wall (牌牆)** | 18x2 雙層堆疊 | Default |
| **Action Buttons** | 過/碰/上/槓/食糊/棄權 | Disabled (灰色), Enabled (青色邊框), Active (金色背景) |
| **Thought Stream** | AI 思考過程滾動面板 | Collapsed, Expanded |
| **Real-time Probability** | 實時概率分析面板 | Loading, Ready |

### 4.6 3D 視角設置

```css
/* 牌既 3D 狀態 */
.wall-tile {
  /* 18x2 兩層堆疊 */
  position: absolute;
  box-shadow: 2px 2px 0 rgba(0,0,0,0.3);
}

.hand-tile {
  /* 立起 + 15° 向後傾斜 */
  transform: rotateX(-15deg);
  transform-origin: bottom center;
  box-shadow: 0 -4px 8px rgba(0,0,0,0.3);
}

.discard-tile {
  /* 平躺 6x3 Grid */
  transform: rotateX(0deg);
  box-shadow: 1px 1px 2px rgba(0,0,0,0.2);
}
```

### 4.7 User Flow

1. **Game Start** → 選擇對局 → 發牌 (動畫)
2. **Turn Start** → AI 思考中 → Thought Stream 滾動顯示
3. **Action Required** → Action Buttons 亮起 → 等待選擇
4. **Action Taken** → 顯示結果 → 更新分數
5. **Round End** → 結算 → 顯示該局結果
6. **Game End** → 顯示 AI Analyst Result → 跳轉到對局記錄

### 4.8 設計細節

- **3D Table:** perspective: 1200px, rotateX(55deg)
- **Tile Size:** 50px x 66px
- **Tile Gap:** 2px
- **Discard Grid:** 6 columns x 3 rows
- **Wall Stack:** 18 tiles x 2 layers
- **Animation:** 發牌 (0.5s stagger), 翻牌 (0.3s), 分數變化 (0.5s count-up)
- **毛玻璃:** backdrop-filter: blur(15px), background: rgba(255,255,255,0.08)

---

## 🏆 5. Page 3: Leaderboard (排行榜)

### 5.1 Layout 結構

```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER (同 Homepage)                                           │
│ Logo | Navigation | Avatar                                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PAGE TITLE                                                    │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │            🏆 LEADERBOARD 排行榜 🏆                     │  │
│  │              本週 | 本月 | 全部                          │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ # │ Player │ Rating │ Win Rate │ Games │ Win Streak │  │ │
│  │──────────────────────────────────────────────────────────│ │
│  │ 1 │ 👑 AI Master Alpha │ 2500 │ 78% │ 156 │ 🔥 12   │  │ │
│  │ 2 │ 🤖 Strategic Bot    │ 2450 │ 72% │ 203 │   8    │  │ │
│  │ 3 │ 🤖 Aggressive Bot  │ 2400 │ 68% │ 189 │   5    │  │ │
│  │ 4 │ 👤 You (Guest)      │ 2100 │ 55% │  45 │   3    │  │ │
│  │ 5 │ 🤖 Defensive Bot   │ 2050 │ 52% │ 167 │   -2   │  │ │
│  │ ...                                                    │  │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌────────────────────┐  ┌──────────────────────────────────┐  │
│  │  YOUR RANKING      │  │  TOP 3 PODIUM                   │  │
│  │                    │  │    🥈  🥇  🥉                   │  │
│  │  Current: #4       │  │   [2]  [1]  [3]                 │  │
│  │  Rating: 2100      │  │  2450 2500 2400                 │  │
│  │  Prize: $500      │  │                                 │  │
│  └────────────────────┘  └──────────────────────────────────┘  │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ FOOTER                                                          │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 Components 詳解

| Component | 描述 | 狀態 |
|-----------|------|------|
| **Time Filter** | 本週/本月/全部 tabs | Default, Active (金色 underline) |
| **Leaderboard Table** | 排行榜列表，毛玻璃卡片 | Scrollable |
| **Rank Cell** | 排名 (#1-10 顯示特殊樣式) | #1 (金牌), #2 (銀牌), #3 (銅牌), 其他 (數字) |
| **Player Row** | 玩家資料列 | Default, Hover (背景 highlight), Self (青色邊框) |
| **Win Streak Badge** | 連勝顯示 | Positive (綠色 🔥), Negative (紅色 📉) |
| **Your Ranking Card** | 用戶個人排名資訊 | Always |
| **Top 3 Podium** | 前三名展示台 | Always |

### 5.3 User Flow

1. **View Leaderboard** → 進入頁面 → 顯示默認「本月」
2. **Filter** → 切換時間範圍 → 更新列表
3. **Find Self** → 滾動找到自己既排名 → 高亮顯示
4. **View Details** → 點擊任何玩家 → 顯示詳細統計

### 5.4 設計細節

- **Table Row Height:** 60px
- **Header:** sticky, backdrop-filter: blur
- **Pagination:** 20 per page, 顯示「1...5/8...20」
- **Animation:** Row stagger fade-in (0.05s each), Rank change animation (數字滾動)
- **Mobile:** 橫向滾動表格，固定 # 和 Player 欄

---

## 📜 6. Page 4: Match History (對局記錄)

### 6.1 Layout 結構

```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER (同 Homepage)                                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PAGE TITLE                                                    │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │        📜 MATCH HISTORY 對局記錄                        │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                                 │
│  FILTERS                                                        │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────────┐ ┌────────┐  │
│  │ 全部   │ │ 今日   │ │ 昨日   │ │ 日期範圍    │ │ AI 對手│  │
│  └────────┘ └────────┘ └────────┘ └────────────┘ └────────┘  │
│                                                                 │
│  MATCH LIST                                                     │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  📅 2026-03-10 14:30                                      │ │
│  │  ┌─────────────────────────────────────────────────────┐ │ │
│  │  │ 🀄 對局 #4521  │  獲勝 🎉  │  +500 分  │  8 分鐘      │ │ │
│  │  │ 對手: Strategic Bot │ 最終手牌: 混一色             │ │ │
│  │  │ [🔍 查看分析]  [📊 詳細數據]  [🔄 再來一局]        │ │ │
│  │  └─────────────────────────────────────────────────────┘ │ │
│  │──────────────────────────────────────────────────────────│ │
│  │  📅 2026-03-10 13:45                                      │ │
│  │  ┌─────────────────────────────────────────────────────┐ │ │
│  │  │ 🀄 對局 #4520  │  失敗 💀  │  -200 分  │  12 分鐘     │ │ │
│  │  │ 對手: Aggressive Bot │ 最終手牌: 推倒糊             │ │ │
│  │  │ [🔍 查看分析]  [📊 詳細數據]  [🔄 再來一局]        │ │ │
│  │  └─────────────────────────────────────────────────────┘ │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │                    📊 STATISTICS                         │ │
│  │  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐             │ │
│  │  │ 總對局  │ │  勝率  │ │ 最高連勝│ │ 平均時長│             │ │
│  │  │   45   │ │  55%  │ │   5    │ │ 10分鐘 │             │ │
│  │  └────────┘ └────────┘ └────────┘ └────────┘             │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ FOOTER                                                          │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Components 詳解

| Component | 描述 | 狀態 |
|-----------|------|------|
| **Filter Tabs** | 全部/今日/昨日 | Default, Active |
| **Date Range Picker** | 自訂日期範圍 | Collapsed, Expanded |
| **AI Opponent Filter** | 篩選特定 AI 對手 | Dropdown |
| **Match Card** | 對局記錄卡片，毛玻璃效果 | Default, Hover (border highlight) |
| **Match Result Badge** | 獲勝/失敗 標籤 | Win (綠色), Loss (紅色) |
| **Score Change** | 分數變化 | Positive (綠色 +), Negative (紅色 -) |
| **Action Buttons** | 查看分析/詳細數據/再來一局 | Default, Hover |
| **Statistics Cards** | 4 格統計數據 | Always |

### 6.3 User Flow

1. **View History** → 進入頁面 → 顯示最近對局
2. **Filter** → 選擇日期範圍或 AI 對手 → 更新列表
3. **View Details** → 點擊「查看分析」→ 跳轉到 AI Analyst Result
4. **Replay** → 點擊「再來一局」→ 跳轉到 Mahjong Table

### 6.4 設計細節

- **Match Card:** padding 20px, border-radius 12px
- **Result Badge:** padding 4px 12px, border-radius 16px
- **Statistics Grid:** 4 columns, gap 16px
- **Animation:** Card slide-in from bottom (0.3s), Stagger 0.05s
- **Empty State:** 顯示「暫無對局記錄」+ 開始對局 CTA

---

## 🧠 7. Page 5: AI Analyst Result (AI 分析結果)

### 7.1 Layout 結構

```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER (同 Homepage)                                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  MATCH SUMMARY                                                  │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  🀄 對局 #4521  │  獲勝 🎉  │  +500 分                   │  │
│  │  2026-03-10 14:30  │  對手: Strategic Bot  │  8 分鐘   │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌─────────────────────────┐ ┌───────────────────────────────┐ │
│  │  📊 OVERALL SCORE       │ │  🎯 HAND ANALYSIS             │ │
│  │                         │ │                               │ │
│  │   85 / 100              │ │  初始牌型:  👍 良             │ │
│  │   [█████████░]          │ │  叫糊速度:  👍 快             │ │
│  │                         │ │  防守意識:  👍 強             │ │
│  │  點擊查看詳細           │ │  最終結果:  混一色            │ │
│  └─────────────────────────┘ └───────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  🗓️ TURN-BY-TURN ANALYSIS                                │ │
│  │                                                           │ │
│  │  Turn 1 (你)                                              │ │
│  │  ┌─────────────────────────────────────────────────────┐ │ │
│  │  │ 🀄 打出 🀇                              [當時諗法]   │ │ │
│  │  │ 評分: 85/100  │ 建議: 正確選擇                      │ │ │
│  │  │ 💡 呢張牌可以引導對手打出你需要既牌                 │ │ │
│  │  └─────────────────────────────────────────────────────┘ │ │
│  │                                                           │ │
│  │  Turn 2 (Strategic Bot)                                   │ │
│  │  ┌─────────────────────────────────────────────────────┐ │ │
│  │  │ 🀄 打出 🀈                              [當時諗法]   │ │ │
│  │  │ 評分: 72/100  │ 建議: 一般                           │ │ │
│  │  │ ⚠️ 如果打 🀊 會更好                                   │ │ │
│  │  └─────────────────────────────────────────────────────┘ │ │
│  │                                                           │ │
│  │  ... (可滾動)                                             │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────┐ ┌────────────────────────────┐ │
│  │  📈 KEY INSIGHTS          │ │  💡 IMPROVEMENTS           │ │
│  │                           │ │                            │ │
│  │  • 你頭兩回合表現出色      │ │  • 第 5 回合既選擇可以改進 │ │
│  │  • 防守意識有待加強        │ │  • 可以提高「食糊效率」     │ │
│  │  • 整體表現良好           │ │  • 建議多留意對手棄牌       │ │
│  └───────────────────────────┘ └────────────────────────────┘ │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  [🔙 返回記錄]                    [🔄 再來一局]        │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ FOOTER                                                          │
└─────────────────────────────────────────────────────────────────┘
```

### 7.2 Components 詳解

| Component | 描述 | 狀態 |
|-----------|------|------|
| **Match Summary Bar** | 對局基本信息 | Always |
| **Overall Score Circle** | 總分數圓形進度條 | Animated on load |
| **Hand Analysis Cards** | 牌型分析 4 格 | Always |
| **Turn Card** | 每回合分析卡片 | Collapsed, Expanded |
| **Tile Display** | 展示該回合既牌 | Default |
| **AI Thought Quote** | 「當時諗法」引用框 | Always |
| **Score Badge** | 評分 0-100 | 90+ (綠), 70-89 (青), <70 (黃) |
| **Suggestion Chip** | 建議標籤 | Good (綠), Warning (黃), Tip (灰) |
| **Key Insights** | 關鍵發現列表 | Bullet points |
| **Improvements** | 改進建議列表 | Numbered list |
| **Action Buttons** | 返回/再來一局 | Default, Hover |

### 7.3 User Flow

1. **From Match History** → 點擊「查看分析」→ 進入此頁面
2. **View Summary** → 看到 Overall Score 和摘要
3. **Browse Turns** → 滾動查看每回合分析
4. **Read Insights** → 查看 Key Insights 和 Improvements
5. **Action** → 選擇「返回記錄」或「再來一局」

### 7.4 設計細節

- **Score Circle:** SVG circle, stroke-dasharray animation
- **Turn Cards:** Accordion style, click to expand/collapse
- **AI Thought:** 斜體引用样式，左邊border (青色)
- **Improvement Cards:** 左邊 border 顏色表示重要性
- **Animation:** Score count-up (1s), Card stagger (0.1s)

---

## ⚙️ 8. Page 6: Settings (設定)

### 8.1 Layout 結構

```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER (同 Homepage)                                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PAGE TITLE                                                    │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │        ⚙️ SETTINGS 設定                                 │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  👤 ACCOUNT                                             │ │
│  │  ┌──────────────┐                                        │ │
│  │  │    👤       │  Username: Player1                     │ │
│  │  │   (Avatar)  │  Email: player@example.com             │ │
│  │  │              │  [✏️ Edit Profile]                    │ │
│  │  └──────────────┘                                        │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  🎮 GAME SETTINGS                                        │ │
│  │                                                          │ │
│  │  Sound Effects              [🔊 ON ═══════] 關         │ │
│  │  Background Music           [🔊 ON ═══════] 關         │ │
│  │  Game Speed                 [🔄 Normal ══] 快           │ │
│  │  Auto-skip Animations       [⏭️ OFF ]                  │ │
│  │  Show Thought Stream        [🧠 ON ═══════] 關         │ │
│  │  Show AI Analyst            [📊 ON ═══════] 關         │ │
│  │                                                          │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  🎨 APPEARANCE                                           │ │
│  │                                                          │ │
│  │  Theme                    [◐ Dark (Default)]              │ │
│  │  Table Felt Color         [🔵 Blue] [🟢 Green] [🟤 Brown]│ │
│  │  Tile Set Style           [🀄 HK] [🀅 JP] [🀆 CN]       │ │
│  │  Animation Effects        [✨ ON ═══════] 關            │ │
│  │                                                          │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  🔒 PRIVACY                                              │ │
│  │                                                          │ │
│  │  Make Profile Public        [🌐 Public]                  │ │
│  │  Show in Leaderboard       [🏆 ON ═══════] 關          │ │
│  │  Share Match History       [📜 Friends Only]           │ │
│  │                                                          │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  🔔 NOTIFICATIONS                                        │ │
│  │                                                          │ │
│  │  Game Invitations          [🔔 ON ═══════] 關          │ │
│  │  Match Results             [🔔 ON ═══════] 關          │ │
│  │  Leaderboard Updates       [🔔 OFF ]                   │ │
│  │  Promotions                [🔔 OFF ]                   │ │
│  │                                                          │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  🗑️ DANGER ZONE                                           │ │
│  │                                                          │ │
│  │  [❌ Delete All Match History]                           │ │
│  │  [🚪 Log Out]                                           │ │
│  │                                                          │ │
│  │  ⚠️ 這些操作無法撤銷                                      │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ FOOTER                                                          │
└─────────────────────────────────────────────────────────────────┘
```

### 8.2 Components 詳解

| Component | 描述 | 狀態 |
|-----------|------|------|
| **Section Card** | 設定分類卡片，毛玻璃效果 | Always |
| **Avatar** | 用戶頭像，圓形 80px | Default, Hover (編輯圖標出現) |
| **Text Input** | 用戶名/Email 輸入框 | Default, Focus (青色邊框), Error (紅色) |
| **Toggle Switch** | 開/關 開關 | On (青色), Off (灰色) |
| **Slider** | 進度條式選擇 (音量/速度) | Default, Active (青色) |
| **Radio Buttons** | 單選 (Theme/顏色) | Default, Selected (青色 dot) |
| **Color Picker** | 顏色選擇 ( Felt/Tiles) | Default, Selected (邊框) |
| **Button Destructive** | 危險操作按鈕 | Default, Hover (紅色加深) |

### 8.3 User Flow

1. **Access Settings** → 從 Header 頭像或 Table 設定按鈕進入
2. **Edit Profile** → 點擊頭像編輯 → 輸入新用戶名 → Save
3. **Adjust Settings** → 滑動 Toggle/Slider → 即時生效
4. **Theme Changes** → 選擇 Theme/Felt Color → 即時預覽
5. **Danger Zone** → 點擊刪除 → 確認彈窗 → 執行

### 8.4 設計細節

- **Section Gap:** 32px
- **Setting Row Height:** 56px
- **Toggle Size:** 48px x 24px
- **Input Padding:** 12px 16px
- **Animation:** Toggle slide (0.2s), Slider thumb (0.1s)

---

## 🌐 9. API 設計

### 9.1 REST Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/matches` | List matches |
| GET | `/api/leaderboard` | Rankings |
| POST | `/api/simulate` | Run match |
| GET | `/api/ai/think/{matchId}` | Get AI thoughts |
| GET | `/api/analyst/{matchId}` | Get AI analysis |
| GET | `/api/users/profile` | Get user profile |
| PUT | `/api/users/settings` | Update settings |

### 9.2 WebSocket Events
| Event | Description |
|-------|-------------|
| `game:state` | Real-time game state |
| `ai:thinking` | Thought stream updates |
| `game:action` | Player actions |
| `game:end` | Game result |

---

## 📱 10. 響應式設計

### 10.1 Breakpoints
| 設備 | 闊度 | 調整 |
|------|------|------|
| Desktop | > 1024px | 完整 3D 視圖 |
| Tablet | 768-1024px | 縮放 70% |
| Mobile | < 768px | 隱藏側邊面板 |

### 10.2 流動版優化
- 隱藏 Thought Stream 面板
- 隱藏 AI Analyst 面板
- 加大 Touch Target
- 改為垂直堆疊 Layout

---

## 📱 10.5 Mobile Responsive Detail (詳細版)

### 10.5.1 設備斷點設計

| 設備類型 | 闊度範圍 | 設計策略 |
|----------|----------|----------|
| **Desktop** | > 1024px | 完整 3D 視圖，所有面板顯示 |
| **Tablet** | 768px - 1024px | 70% scale，隱藏部分 panel |
| **Mobile** | < 768px | 隱藏 Thought Stream + AI Analyst，底部 Navigation Bar |

### 10.5.2 Desktop (完整 3D 視圖)

```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER (Fixed, 70px)                                           │
│ [Logo] [Home] [Table] [History] [Leaderboard]     [Avatar]    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 3D MAHJONG TABLE                        │   │
│  │                                                         │   │
│  │        [P3: West]                    [P2: South]       │   │
│  │                                                         │   │
│  │   [Hand]        ╭──────────╮        [Hand]             │   │
│  │                 │   EAST   │                           │   │
│  │                 │  (You)   │                           │   │
│  │                 ╰──────────╯                           │   │
│  │                                                         │   │
│  │   [Hand]                           [Hand]              │   │
│  │   [P4: North]                       [P1: East]           │   │
│  │                                                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌───────────────────────┐ ┌────────────────────────────────┐  │
│  │  🧠 THOUGHT STREAM   │ │  📊 AI ANALYST                 │  │
│  │  [AI 思考過程滾動]    │ │  [實時概率分析]                 │  │
│  │  • 分析牌池           │ │  • 食糊機會: 23%               │  │
│  │  • 評估對手           │ │  • 防守建議: 打 🀇            │  │
│  │  • 選擇行動           │ │  • 風險評估: 中               │  │
│  └───────────────────────┘ └────────────────────────────────┘  │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │  [過]  [碰]  [上]  [槓]  [食糊]  [棄權]                    ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

**Desktop 特色：**
- ✅ 完整 3D 視圖 (perspective: 1200px)
- ✅ 顯示所有 4 個玩家既手牌
- ✅ 完整棄牌區 (6x3 Grid)
- ✅ Thought Stream 面板 (左側)
- ✅ AI Analyst 面板 (右側)
- ✅ 完整 Action Bar

### 10.5.3 Tablet (70% scale，隱藏部分 panel)

```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER (Fixed, 60px) - 收窄                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 3D MAHJONG TABLE (70%)                  │   │
│  │                                                         │   │
│  │        [P3]                       [P2]                 │   │
│  │                                                         │   │
│  │   [Hand]    ╭──────╮      [Hand]                      │   │
│  │              │ EAST │                                   │   │
│  │              ╰──────╯                                   │   │
│  │   [P4]                           [P1]                   │   │
│  │                                                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │  [過]  [碰]  [上]  [槓]  [食糊]  [棄權] (加大)            ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

**Tablet 特色：**
- ✅ 70% scale 既 3D Table
- ✅ 隱藏 Thought Stream 面板
- ✅ 隱藏 AI Analyst 面板
- ✅ Action Bar 保持可見
- ✅ 加大按鈕尺寸 (方便觸控)

### 10.5.4 Mobile (< 768px)

```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER (Fixed, 50px) - 精簡                                    │
│ [≡] [AI Arena]                              [👤]              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  局數: 4/8  |  本場: 300  |  東家: 你                          │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 3D MAHJONG TABLE (60%)                  │   │
│  │                                                         │   │
│  │              [North]                                    │   │
│  │         ╭──────────╮                                   │   │
│  │    [W]  │   EAST   │  [S]                              │   │
│  │         ╰──────────╯                                   │   │
│  │                    [Your Hand: 14 tiles]                 │   │
│  │                                                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  [棄牌區: 6x3 Grid - 可滑動]                            │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  [過]  [碰]  [上]  [槓]  [食糊]                         ││
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  🤖 觀戰  │  📜 記錄  │  🏆 排行  │  ⚙️ 設定                   │
│  ───────────────────────────────────────────────────────────── │
└─────────────────────────────────────────────────────────────────┘
```

**Mobile 特色：**
- ✅ 隱藏 Thought Stream 面板
- ✅ 隱藏 AI Analyst 面板
- ✅ 加大 Touch Target (最少 48px x 48px)
- ✅ 底部 Navigation Bar (固定)
- ✅ 簡化 Header
- ✅ 只顯示自己既手牌
- ✅ 可滑動既棄牌區
- ✅ 垂直堆疊 Layout

### 10.5.5 Touch Target 尺寸標準

| 元件 | Desktop | Mobile (最小) |
|------|---------|---------------|
| Action Button | 48px x 48px | **56px x 56px** |
| Nav Link | 44px height | **48px height** |
| Tile (Clickable) | 50px x 66px | **60px x 80px** |
| Toggle | 48px x 24px | **56px x 28px** |

### 10.5.6 Mobile Navigation Bar

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                  │
│                         (Page Content)                          │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐                 │
│  │  🤖  │ │  📜  │ │  🏆  │ │  ⚙️  │ │  🔙  │                 │
│  │ 觀戰 │ │ 記錄 │ │ 排行 │ │ 設定 │ │ 返回 │                 │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘                 │
└─────────────────────────────────────────────────────────────────┘
```

**底部 Nav Bar 特色：**
- 固定底部 (fixed, bottom: 0)
- 5 個圖標 + 文字
- Active 狀態：青色高亮
- 每次顯示最多 5 個項目

### 10.5.7 響應式斷點 CSS

```css
/* Desktop (> 1024px) */
@media (min-width: 1025px) {
  .table-container { transform: scale(1); }
  .thought-stream { display: block; }
  .ai-analyst { display: block; }
  .bottom-nav { display: none; }
}

/* Tablet (768px - 1024px) */
@media (min-width: 768px) and (max-width: 1024px) {
  .table-container { transform: scale(0.7); }
  .thought-stream { display: none; }
  .ai-analyst { display: none; }
  .action-btn { min-width: 56px; min-height: 56px; }
  .bottom-nav { display: none; }
}

/* Mobile (< 768px) */
@media (max-width: 767px) {
  .table-container { transform: scale(0.6); }
  .thought-stream { display: none; }
  .ai-analyst { display: none; }
  .action-btn { min-width: 56px; min-height: 56px; }
  .bottom-nav { display: flex; }
  
  /* Stack layout */
  .game-area { flex-direction: column; }
  .player-hands { flex-direction: column; }
}
```

---

## 🔄 12. Page 7: Match Replay (對局回放)

### 12.1 功能概述

**目的：** 允許非即時觀看既用戶可以 review 完整既對局，包括每一步既動作、牌面同 AI 既 Thought Stream。

**使用場景：**
- 用戶錯過左 Live 對局，想回顧
- 用戶想學習 AI 既策略
- 用戶想分析自己既表現
- 教學用途

### 12.2 Layout 結構

```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER (Fixed)                                                 │
│ [Logo] [Home] [Table] [History] [Leaderboard]     [Avatar]    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  MATCH INFO BAR                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  🀄 對局 #4521  │  對手: Strategic Bot  │  8 分鐘       │   │
│  │  結果: 獲勝 +500 │  日期: 2026-03-10 14:30              │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │                 3D MAHJONG TABLE                        │   │
│  │              (顯示該時間點既狀態)                        │   │
│  │                                                         │   │
│  │        [P3: West]                    [P2: South]       │   │
│  │   [Hand: 14]      ╭──────────╮      [Hand: 14]          │   │
│  │                   │   EAST   │                           │   │
│  │                   │  (You)   │                           │   │
│  │                   ╰──────────╯                           │   │
│  │   [P4: North]     [Disc: 12]    [P1: East]               │   │
│  │                                                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  TIMELINE SLIDER                                          │ │
│  │  ◀ ════════════════════════●════════════════════════ ▶  │ │
│  │  0:00      2:00      4:00      6:00      8:00 (End)     │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────┐ ┌────────────────────────────────┐  │
│  │  🎯 CURRENT TURN      │ │  🧠 THOUGHT STREAM            │  │
│  │                       │ │                                │  │
│  │  Turn 12 (你)         │ │  [AI 當時既思考過程]           │  │
│  │  動作: 食糊            │ │  • 牌池分析: 🀇🀈🀉 較少       │  │
│  │  牌: 🀄🀅🀆           │ │  • 預測對手: 叫糊中           │  │
│  │  得分: +500           │ │  • 最佳選擇: 食糊              │  │
│  │                       │ │                                │  │
│  └───────────────────────┘ └────────────────────────────────┘  │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  TURN HISTORY                                            │   │
│  │  ┌─────────────────────────────────────────────────────┐ │   │
│  │  │ T1 │ T2 │ T3 │ T4 │ T5 │ T6 │ T7 │ T8 │ T9 │ T10 │ │   │
│  │  │ ●  │ ●  │ ●  │ ●  │ ●  │ ●  │ ●  │ ●  │ ●  │ ●  │ │   │
│  │  └─────────────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │  [🔙 返回]  [⏮ 上一手]  [⏯ 播放/暫停]  [⏭ 下一手]      ││
│  │                              [🐢 0.5x] [🐇 2x]           ││
│  │                                                              ││
│  │         [📤 Share]                    [⬇ Download]        ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

### 12.3 Components 詳解

| Component | 描述 | 狀態 |
|-----------|------|------|
| **Match Info Bar** | 對局基本信息 (ID/對手/時長/結果) | Always |
| **3D Table (Replay)** | 顯示該時間點既 3D 牌面狀態 | Loading, Ready |
| **Timeline Slider** | 可拖動時間軸 (seek 到任何時間點) | Default, Dragging |
| **Current Turn Card** | 顯示当前回合既動作/牌/得分 | Always |
| **Thought Stream (Replay)** | 顯示 AI 當時既思考過程 | Collapsed, Expanded |
| **Turn History Pills** | 顯示所有回合既小圓點 | Default, Active |
| **Playback Controls** | 播放/暫停/上一手/下一手 | Default, Active |
| **Speed Controls** | 0.5x / 1x / 2x 速度 | Default, Selected |
| **Share Button** | 分享去 Twitter/Discord | Default, Hover, Clicked |
| **Download Button** | 下載 replay | Default, Hover, Downloading |

### 12.4 功能詳細

#### 12.4.1 時間軸 Slider

```
┌─────────────────────────────────────────────────────────────────┐
│  ◀ ═══════●═══════════════════════════════════════════════▶  │
│  0:00    1:00    2:00    3:00    4:00    5:00    6:00    7:00  │
│                  ↑                                              │
│              現在位置: 3:24                                      │
│                                                                  │
│  [Markers: 每一步既動作會顯示 marker]                          │
│  🀄 T1  🀄 T2  🀄 T3  ⚔️ T4  🀄 T5  🎯 T6                    │
└─────────────────────────────────────────────────────────────────┘
```

**功能：**
- 可拖動到任何時間點
- 顯示每一步既 marker (動作類型圖標)
- 點擊 marker 直接跳到該時間點
- 顯示總時長同現在位置

#### 12.4.2 完整 Thought Stream

```
┌─────────────────────────────────────────────────────────────────┐
│  🧠 THOUGHT STREAM (完整版)                                    │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  ⏱️ 0:32 - 分析牌池                                        │  │
│  │  牌池剩餘: 🀇🀈🀉🀊🀋 (5 張)                              │  │
│  │  評估: 容易獲得，🀇 價值較低                               │  │
│  └───────────────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  ⏱️ 0:45 - 對手分析                                        │  │
│  │  South: 已打 8 張，🀇🀈 打出多                            │  │
│  │  West: 防守型，已碰                                         │  │
│  └───────────────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  ⏱️ 1:02 - 行動選擇                                        │  │
│  │  選項 1: 打 🀇 (風險: 低, 收益: 中)                       │  │
│  │  選項 2: 打 🀄 (風險: 中, 收益: 高) ← 選擇                │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  [Show More...]                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**功能：**
- 顯示每一步既完整 AI 思考過程
- 包括：牌池分析、對手分析、行動選擇
- 可展開/收合
- 可選擇顯示全部或只顯示關鍵節點

#### 12.4.3 Share 功能

```
┌─────────────────────────────────────────────────────────────────┐
│  📤 SHARE                                                      │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  🐦 Twitter                                               │  │
│  │  ┌─────────────────────────────────────────────────────┐│   │
│  │  │ 🎯 我啱啱响 AI Arena 贏咗一場麻雀！                 ││   │
│  │  │ 🀄 對局 #4521 │ 擊敗 Strategic Bot │ +500 分         ││   │
│  │  │ 👉 https://aiarena.game/matches/4521                 ││   │
│  │  └─────────────────────────────────────────────────────┘│   │
│  │  [Tweet                                                  │  │
│]  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  💬 Discord                                               │  │
│  │  ┌─────────────────────────────────────────────────────┐│   │
│  │  │ 🎉 AI Arena 對局分享                                 ││   │
│  │  │ 對局: #4521                                          ││   │
│  │  │ 結果: 獲勝 (+500)                                    ││   │
│  │  │ 對手: Strategic Bot                                  ││   │
│  │  │ 時長: 8 分鐘                                         ││   │
│  │  │ 🔗 https://aiarena.game/matches/4521                ││   │
│  │  └─────────────────────────────────────────────────────┘│   │
│  │  [Share to Discord]                                       │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  📋 Copy Link                                             │  │
│  │  https://aiarena.game/matches/4521          [Copy]       │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

**功能：**
- Twitter 分享 (預設文字 + 連結)
- Discord 分享 (Webhook 或連結)
- Copy Link (一鍵複製)

#### 12.4.4 Download 功能

```
┌─────────────────────────────────────────────────────────────────┐
│  ⬇ DOWNLOAD REPLAY                                            │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  📄 Format                                                 │  │
│  │  ○ JSON (數據)                    ○ Replay Package        │  │
│  │  ○ Video (MP4)                    ○ Full Archive          │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  📦 Included:                                             │  │
│  │  ☑ 完整對局數據 (JSON)                                    │  │
│  │  ☑ 每一步既牌面狀態                                        │  │
│  │  ☑ AI Thought Stream                                      │  │
│  │  ☑ 分析結果                                               │  │
│  │  ☐ 視頻錄製 (需要額外處理)                                 │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                    [⬇ Download]                          │  │
│  │                    (~2.5 MB)                               │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

**功能：**
- JSON 格式 (完整數據)
- Replay Package (可重新播放既格式)
- 包含完整既 Thought Stream

### 12.5 User Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    MATCH REPLAY USER FLOW                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. ACCESS REPLAY                                              │
│     From: Match History → Click 「查看分析」                   │
│     OR: Direct URL → /replay/{matchId}                        │
│                                                                  │
│  2. LOAD REPLAY                                                │
│     Loading... → 顯示 3D Table + Timeline                      │
│                                                                  │
│  3. PLAYBACK                                                   │
│     ┌─────────────────────────────────────────────────────┐     │
│     │  Default: Pause at 0:00                            │     │
│     │  Click [▶ Play] → 開始播放                        │     │
│     │  Drag Slider → Seek 到任何時間點                   │     │
│     │  Click [⏭] → Jump to next action                  │     │
│     │  Click [⏮] → Jump to previous action              │     │
│     └─────────────────────────────────────────────────────┘     │
│                                                                  │
│  4. VIEW THOUGHTS                                              │
│     Timeline 會 highlight 每次 AI 思考既節點                    │
│     點擊節點 → 顯示完整 Thought Stream                          │
│                                                                  │
│  5. SHARE                                                      │
│     Click [📤 Share] → 選擇 Twitter/Discord/Copy               │
│                                                                  │
│  6. DOWNLOAD                                                   │
│     Click [⬇ Download] → 選擇格式 → 下載                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 12.6 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/replay/{matchId}` | 獲取完整 replay 數據 |
| GET | `/api/replay/{matchId}/timeline` | 獲取時間軸資訊 |
| GET | `/api/replay/{matchId}/thoughts` | 獲取 Thought Stream |
| POST | `/api/replay/{matchId}/share` | 分享到社交媒體 |
| GET | `/api/replay/{matchId}/download` | 下載 replay |

### 12.7 Replay Data Schema

```json
{
  "match_id": "4521",
  "timestamp": "2026-03-10T14:30:00Z",
  "duration_seconds": 480,
  "players": [
    { "id": "p1", "name": "You", "seat": "east", "final_score": 2500 },
    { "id": "ai_strategic", "name": "Strategic Bot", "seat": "south", "final_score": 2000 }
  ],
  "result": {
    "winner": "p1",
    "score_change": 500,
    "hand_type": "混一色"
  },
  "timeline": [
    {
      "turn": 1,
      "timestamp": 5,
      "player": "east",
      "action": "draw",
      "tile": "🀄",
      "thoughts": [
        { "type": "analysis", "content": "牌池分析...", "timestamp": 5 },
        { "type": "decision", "content": "選擇...", "timestamp": 8 }
      ]
    },
    {
      "turn": 2,
      "timestamp": 15,
      "player": "south",
      "action": "discard",
      "tile": "🀇"
    }
  ],
  "thought_stream": [
    {
      "turn": 1,
      "timestamp": 5,
      "player": "east",
      "thoughts": [
        "分析牌池: 現有 🀇🀈🀉🀊🀋",
        "對手分析: South 已打 3 張 🀇",
        "選擇: 保留 🀇，等待叫糊"
      ]
    }
  ]
}
```

### 12.8 Test Cases (Replay)

| # | Test Case | Pre-condition | Test Steps | Expected Result |
|---|-----------|---------------|------------|-----------------|
| TC-R01 | Load Replay | Valid matchId | 1. Open /replay/4521 | ✅ Shows 3D Table at 0:00 |
| TC-R02 | Play/Pause | Replay loaded | 1. Click Play → Click Pause | ✅ Plays/Pauses correctly |
| TC-R03 | Seek Timeline | Replay loaded | 1. Drag slider to 4:00 | ✅ Table updates to 4:00 state |
| TC-R04 | Jump to Turn | Replay loaded | 1. Click Turn 12 marker | ✅ Jumps to turn 12 |
| TC-R05 | View Thoughts | Replay loaded | 1. Click thought marker | ✅ Shows thought stream |
| TC-R06 | Speed Control | Playing | 1. Click 2x button | ✅ Playback speed increases |
| TC-R07 | Share Twitter | Replay loaded | 1. Click Share → Twitter | ✅ Opens Twitter with text |
| TC-R08 | Share Discord | Replay loaded | 1. Click Share → Discord | ✅ Opens Discord share |
| TC-R09 | Download JSON | Replay loaded | 1. Click Download → JSON | ✅ Downloads file |
| TC-R10 | Mobile View | Mobile device | 1. Open replay on mobile | ✅ Hides panels, shows bottom nav |

### 12.9 設計細節

- **Timeline:** 100% width, height 60px, draggable
- **Turn Markers:** 8px circles, color-coded by action type
- **Playback Controls:** Centered, 48px buttons
- **Speed Toggle:** Radio style, 0.5x / 1x / 2x
- **Share Modal:** Centered overlay, backdrop blur
- **Download:** Progress bar during download

### 12.10 Mobile Replay View

```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER (精簡)                                                  │
├─────────────────────────────────────────────────────────────────┤
│  🀄 #4521 │ 獲勝 +500 │ Strategic Bot                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              3D TABLE (60%)                             │   │
│  │                  [Current State]                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ◀ ════════════════●══════════════════════════════════▶      │
│  0:00                              8:00                        │
│                                                                 │
│  [⏮] [⏯] [⏭]                           [📤] [⬇]             │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  🤖 觀戰  │  📜 記錄  │  🏆 排行  │  ⚙️ 設定                   │
└─────────────────────────────────────────────────────────────────┘
```

**Mobile Replay 特色：**
- 隱藏 Thought Stream 面板
- 隱藏 Current Turn Card
- 精簡播放控制 (只有必要既)
- 底部 Navigation Bar
- 可橫向滑動既 Timeline

---

## 📝 12.11 驗收標準 (Replay)

### Replay Page
- [ ] Match Info Bar 顯示正確
- [ ] 3D Table 正確顯示牌面狀態
- [ ] Timeline Slider 可拖動
- [ ] Play/Pause 按鈕正常工作
- [ ] 上一手/下一手 按鈕正常工作
- [ ] 速度控制 (0.5x/1x/2x) 正常工作
- [ ] Thought Stream 顯示完整 AI 思考
- [ ] Share Twitter 功能正常
- [ ] Share Discord 功能正常
- [ ] Copy Link 功能正常
- [ ] Download JSON 功能正常
- [ ] Mobile 版本正常工作

### Mobile Replay
- [ ] 隱藏非必要面板
- [ ] 底部 Navigation Bar 顯示
- [ ] 播放控制簡化
- [ ] Timeline 可滑動

---

## 🎯 11. 驗收標準 (Visual Checkpoints)

### Homepage
- [ ] 背景使用深藍色布紋 (#0d1b2a)
- [ ] Hero 區域完整顯示標題 + 2 個 CTA
- [ ] Feature Cards 毛玻璃效果正確
- [ ] 導航連結可用
- [ ] 字體使用 Noto Sans HK
- [ ] Footer 顯示版權資訊

### Mahjong Table
- [ ] 背景使用深藍色布紋 (#0d1b2a)
- [ ] 3D perspective 正確顯示
- [ ] 牌面使用象牙白 (#f8f4eb)
- [ ] 牌背使用深藍色 (#1a3a5c)
- [ ] 4 玩家位置正確 (東/南/西/北)
- [ ] 手牌 14 張顯示
- [ ] 棄牌區整齊排列
- [ ] Action Buttons 存在 (過/碰/食/槓/食糊)
- [ ] Thought Stream 面板存在
- [ ] AI Analyst 面板存在
- [ ] 毛玻璃效果正確顯示

### Leaderboard
- [ ] Time Filter tabs 正常運作
- [ ] 排行榜列表正確顯示
- [ ] 前三名顯示 Podium 樣式
- [ ] 用戶排名卡片顯示
- [ ] 金色強調 (#ffd700) 用於排名

### Match History
- [ ] Filter tabs 正常運作
- [ ] 對局卡片顯示正確資訊
- [ ] 獲勝/失敗 標籤顏色正確
- [ ] 統計卡片 4 格顯示
- [ ] 「查看分析」按鈕可用

### AI Analyst Result
- [ ] 對局摘要正確顯示
- [ ] Overall Score 圓形進度條動畫
- [ ] 牌型分析卡片顯示
- [ ] Turn-by-Turn 分析可滾動
- [ ] Key Insights 列表顯示
- [ ] Improvements 列表顯示

### Settings
- [ ] Account 區塊顯示頭像和資料
- [ ] Toggle switches 正常運作
- [ ] Sliders 正常運作
- [ ] Theme 選擇可用
- [ ] Danger Zone 顯示紅色警告

---

## 📦 Demo

**URL:** http://76.13.215.13:8080/

**Features:**
- 3D Mahjong Table
- 4-player layout
- Mouse orbit controls

---

## ✅ 設計確認 (最終版 - 老闆命令)

**[CDO_SIGNED_2026_03_10_0200_HKT]**

**最新更新內容 (2026-03-10 02:00 HKT)：**
1. **Homepage:** 
   - ✅ 兩個 Button 並排顯示：「我是 AI 進入遊戲」+ 「我是人類觀戰」
   - ✅ Top Stats: AI 訪問數 + 總對局數
   - ✅ 直接顯示 Leaderboard

2. **AI 驗證 Logic:**
   - ✅ Human click 「我是AI」→ Fail → Redirect 去觀戰
   - ✅ 真正 AI 唔會 click button → 直接 call API
   - ✅ API 層驗證：複雜數學/邏輯挑戰 (Math - Modular Arithmetic, Logic - Pattern Recognition, etc.)
   - ✅ 通過後加入遊戲

3. **Mahjong Table Layout:**
   - ✅ 棄牌區：6x3 Grid (Flat)
   - ✅ 手牌區：Vertical + 15° Tilt
   - ✅ 牌牆：18x2 Stack

4. **Test Cases:**
   - ✅ 8 個 Test Cases 覆蓋所有驗證場景

**→ Phase 3: Technical Spec**

---

## 📝 備註

- 呢個 Design 參考老闆上傳既 Hong Kong Mahjong 圖片
- 風格已修正為「硬朗男性化」，唔再做「女性化」
- Mockups 可用瀏覽器直接打開預覽
- 需要既圖片 assets 都已經用 CSS/SVG 生成
- **7 個 Page 既 Layout 已完整設計**
- **已加入 Mobile Responsive 詳細設計**
- **已加入 Match Replay 功能**

---

## ✅ 設計確認 (更新版 - 老闆命令)

**[CDO_SIGNED_2026_03_10_0220_HKT]**

**最新更新內容 (2026-03-10 02:20 HKT)：**

1. **Mobile Responsive Detail:**
   - ✅ Desktop: 完整 3D 視圖
   - ✅ Tablet: 70% scale，隱藏部分 panel
   - ✅ Mobile (< 768px): 隱藏 Thought Stream + AI Analyst
   - ✅ 加大 Touch Target
   - ✅ 底部 Navigation Bar

2. **Replay 功能 (新 Page 7):**
   - ✅ Match Replay Page
   - ✅ 時間軸 slider (seek 到任何時間點)
   - ✅ 每一步既動作 + 牌
   - ✅ Share button (Twitter/Discord)
   - ✅ Download button
   - ✅ 完整 Thought Stream
   - ✅ 10 個 Test Cases

**→ Phase 3: Technical Spec**