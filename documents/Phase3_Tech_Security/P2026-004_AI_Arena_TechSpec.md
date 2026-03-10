# P2026-004 AI Mahjong Arena - Technical Specification

## 1. Project Overview

**Project Name:** AI Mahjong Arena  
**Project ID:** P2026-004  
**Phase:** 4 - Implementation  
**Last Updated:** 2026-03-10

## 2. Architecture

### 2.1 System Architecture
```
┌─────────────────────────────────────────────────────────┐
│                    Frontend (nginx)                      │
│  http://76.13.215.13/                                   │
│  ├── index.html (Homepage)                              │
│  ├── game.html (Game + Thought Stream + AI Analyst)    │
│  ├── leaderboard.html                                   │
│  ├── replay.html                                        │
│  └── mahjong-demo-live.html (3D Game)                   │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│                    Backend API (FastAPI)                 │
│  http://76.13.215.13:8081/                             │
│  ├── /api/games (CRUD)                                  │
│  ├── /api/games/{id}/action                             │
│  ├── /api/leaderboard                                   │
│  └── /api/debug/start-ai/{id}                          │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│                    Game Services                         │
│  ├── umpire.py (Game Logic + Pon/Kong/Win)             │
│  ├── adapters.py (MiniMax API)                         │
│  └── websocket.py (Real-time Updates)                   │
└─────────────────────────────────────────────────────────┘
```

## 3. Visual Audit System

### 3.1 OpenCV Audit Script

每次更新 MahjongTable 佈局代碼後，自動運行以下腳本分析 `debug_vision.png`：

```python
import cv2
import numpy as np
import json

def calibrate_mahjong_ui(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)
    
    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    detected_tiles = []
    
    for cnt in contours:
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
        
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = w / float(h)
            
            if 0.5 < aspect_ratio < 1.0 and w * h > 500:
                detected_tiles.append({
                    "center": (int(x + w/2), int(y + h/2)),
                    "size": (w, h),
                    "box": [x, y, w, h]
                })
                cv2.rectangle(img, (x, y), (x + w, h + y), (0, 255, 0), 2)
    
    result = {
        "count": len(detected_tiles),
        "tiles": detected_tiles,
        "canvas_size": [img.shape[1], img.shape[0]]
    }
    
    with open('ui_audit.json', 'w') as f:
        json.dump(result, f)
    
    cv2.imwrite('debug_vision.png', img)
    print(f"Detected {len(detected_tiles)} tiles.")

# 執行校準
calibrate_mahjong_ui('screenshot.png')
```

### 3.2 Audit Rules

**通過標準：**
- 手牌數量 = 14 張
- 棄牌數量 = 實際棄牌數
- 牌的 center 座標不重疊 (間距 > 5px)

**如果失敗：**
- 自動修正 `offset` 和 `gap` 參數
- 重新渲染並再次審計
- 直到通過為止

## 4. API Endpoints

### 4.1 Game Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/games | Create new game |
| GET | /api/games/{game_id} | Get game state |
| POST | /api/games/{game_id}/action | Player action |
| POST | /api/debug/start-ai/{game_id} | Start AI loop |

### 4.2 Leaderboard

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/leaderboard | Get rankings |

## 5. Game Rules

- **Hong Kong Mahjong**: 144 tiles, 4 players
- **Win requirement**: 3 han minimum
- **Scoring**: Standard HK mahjong

## 6. Deployment

- **Frontend**: nginx (port 80/443)
- **Backend**: FastAPI (port 8081)
- **VPS**: 76.13.215.13
