# P004 AI Arena - Changelog

## [2026-03-10] v0.1.1 - 商業模式確認

### 商業模式確認
- ✅ **統一使用 MiniMax API** - 我地既 API，成本最低
- ✅ **遊戲名稱:** 「AI vs AI 麻雀大賽」
- ✅ **收費模式:** 免費觀戰

### 架構簡化
- ✅ **移除其他 API 複雜性** - 只保留 MiniMax
- ✅ **簡化 Model Adapters** - 只有 MiniMaxAdapter
- ✅ **移除 API Key 收集功能** - 統一使用 MiniMax

### 文件更新
- ✅ Tech Spec: 移除 API Keys 收集描述
- ✅ Tech Spec: 更新為統一使用 MiniMax API
- ✅ Tech Spec: 加入「未來規劃 (Backlog)」section
- ✅ Code: 簡化 Model Adapters
- ✅ CHANGELOG: 記錄 decision

---

## [2026-03-10] v0.1.0 - Phase 4 Development

### 新增功能 (New Features)
- ✅ FastAPI 後端架構
- ✅ 裁判伺服器 (The Umpire)
- ✅ 模型適配器 (Model Adapters) - GPT-4o, Claude, Gemini, Llama, MiniMax
- ✅ WebSocket 實時數據流
- ✅ Debug Mode

### Bug 修正 (Bug Fixes)
| 日期 | Issue | 修正 |
|------|-------|------|
| 2026-03-10 | 麻雀牌數量錯誤 (136張) | 改為 144張 (108+28+4+4) |
| 2026-03-10 | 花牌數量錯誤 (8張) | 改為 4張 (梅蘭菊竹) |
| 2026-03-10 | 花牌+季節總數錯誤 | 改為 8張 (花4+季節4) |
| 2026-03-10 | 日本麻雀規則 | 改為廣東麻雀番數表 |
| 2026-03-10 | 移除「寶牌」「立直」 | 改為正確既廣東麻雀規則 |
| 2026-03-10 | 番數上限 | 改為 10番 |
| 2026-03-10 | 番數積分表 | 加入正確既 3-10番 積分 |
| 2026-03-10 | MiniMax 只用於 Debug | 改為可用於 Live Mode |

### 文件修正 (Document Updates)
- ✅ Tech Spec: 廣東麻雀番數表 (完整21項)
- ✅ Tech Spec: 加入番數積分計算表
- ✅ Tech Spec: 加入「可用既 AI 模型」table
- ✅ UI Spec: Homepage 兩個 buttons
- ✅ UI Spec: AI 驗證 logic
- ✅ UI Spec: Mobile Responsive
- ✅ UI Spec: Match Replay 功能

---

## [2026-03-09] v0.0.1 - Phase 2-3

### Phase 2 - UI/UX Design
- ✅ Hong Kong Style Mahjong 設計
- ✅ 深藍色布紋 (#0d1b2a)
- ✅ 象牙白牌面 (#f8f4eb)
- ✅ 毛玻璃效果
- ✅ 6 Pages Mockups

### Phase 3 - Technical Spec
- ✅ 裁判伺服器設計
- ✅ 模型適配器設計
- ✅ WebSocket 設計
- ✅ PostgreSQL + pgvector 設計
- ✅ Deployment Strategy

---

## 待處理 (To Do)
- [ ] 本地測試
- [ ] 部署到 VPS
- [ ] Phase 5 UAT

---

*最後更新: 2026-03-10 03:24 HKT*
