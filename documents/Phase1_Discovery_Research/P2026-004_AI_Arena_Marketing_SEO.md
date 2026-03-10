# P2026-004 AI Arena - Marketing & SEO Strategy

**Project:** AI Arena (AI-powered Mahjong Game)
**Phase:** 1 - Discovery & Research
**Owner:** COO (Fabio-COO)
**Date:** 2026-03-10
**Version:** 1.0

---

## Executive Summary

本文件旨在回答老闆三個核心問題：
1. **點樣比 AI (ChatGPT/Claude) 搵到？** → AI SEO 策略
2. **點樣做到「AI 提到既麻雀遊戲」？** → 品牌權威建立
3. **爆紅既切入點？** → Viral Growth Strategy

---

## 1. AI SEO 策略 - AI 時代既 Search Engine Optimization

### 1.1 核心概念：點解 AI 會提到你？

**AI 搜尋既運作邏輯：**
- AI 回答問題時，會參考訓練數據同埋即時搜尋結果
- 當用戶問「最好既 AI 麻雀遊戲係邊隻？」，AI 會從：
  1. **訓練數據** 中提取權威來源
  2. **RAG (Retrieval-Augmented Generation)** 即時搜尋高排名內容
  3. **社群訊號** (Twitter/X 討論、Reddit 推薦)

### 1.2 我地既 AI SEO 策略

#### A. 內容權威建立 (Content Authority)

| 策略 | 行動項目 | 優先度 |
|------|----------|--------|
| **官方網誌** | 建立 AI Arena Blog，發佈 AI + 麻雀既深度文章 | 🔴 P0 |
| **FAQ 頁面** | 優化「AI Mahjong vs 傳統麻雀」、「AI 點樣提升遊戲體驗」等問題 | 🔴 P0 |
| **技術文檔** | 發佈 AI 算法說明、建立領域權威 | 🟡 P1 |
| **用戶故事** | 收集玩家成功案例、攻略分享 | 🟡 P1 |

#### B. 結構化數據 (Structured Data)

AI 點樣讀取你既網站？需要實施：

```json
{
  "@context": "https://schema.org",
  "@type": "VideoGame",
  "name": "AI Arena",
  "genre": "Mahjong",
  "gamePlatform": ["Web", "Mobile"],
  "description": "AI-powered Mahjong game with intelligent opponents",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "1000"
  }
}
```

#### C. AI 平台監控清單

| AI 平台 | 監控項目 | 優化方法 |
|---------|----------|----------|
| **ChatGPT** | Plugins/Web Browse 結果 | 建立 GPTs plugin、Submit 到 Bing |
| **Claude** | Web Search 結果 | Claude 會用 Perplexity/Tavist 搜尋，確保高排名 |
| **Perplexity** | 來源引用 | 建立 Perplexity 認證頁面、Submit API |
| **Google AI** | SGE (Search Generative Experience) | 優化 E-E-A-T 信號 |

### 1.3 執行路線圖

| Week | 任務 | Deliverable |
|------|------|--------------|
| Week 1-2 | 官網結構化數據實作 | JSON-LD schema 部署完成 |
| Week 3-4 | Blog 內容首批發佈 | 10 篇 AI + 麻雀文章 |
| Week 5-6 | FAQ 頁面優化 | 50+ FAQ questions |
| Week 7-8 | 提交 AI 平台認證 | GPTs Plugin + Perplexity Submit |

---

## 2. Social Media 策略

### 2.1 YouTube 策略

**目標：** 建立「AI 麻雀」領域既 YouTube 權威

| 內容類型 | 頻率 | 目標 views | 病毒潛力 |
|----------|------|------------|----------|
| **AI 對局精華** | 每日 1 條 | 1K-10K | ⭐⭐⭐⭐ |
| **AI 麻雀教學** | 每週 2 條 | 5K-50K | ⭐⭐⭐⭐⭐ |
| **vs 其他玩家** | 每週 1 條 | 10K-100K | ⭐⭐⭐⭐⭐ |
| **開發日誌** | 每週 1 條 | 1K-5K | ⭐⭐ |

**YouTube SEO 優化：**
- 標題：[AI Mahjong] vs [人類冠軍] - 你估誰勝？
- 描述：包含關鍵詞「AI Mahjong Game」「Online Mahjong AI」
- Tags：mahjong, AI game, online mahjong, Chinese mahjong, AI opponent
- 字幕：必须提供 CC 字幕，提升搜尋可見性

### 2.2 Twitter/X 策略

**目標：** 建立 Twitter 社群，成為 AI 麻雀領域既意見領袖

| 內容類型 | 頻率 | 目標 Engagement |
|----------|------|-----------------|
| **遊戲結果分享** | 每日 3-5 條 | ⭐⭐⭐ |
| **AI 對局精彩片段** | 每日 1 條 | ⭐⭐⭐⭐ |
| **互動投票** | 每週 2 條 | ⭐⭐⭐⭐⭐ |
| **thread 教學** | 每週 1 條 | ⭐⭐⭐⭐ |
| **開發者日誌** | 每週 1 條 | ⭐⭐⭐ |

**Twitter SEO 關鍵詞優化：**
- Hashtag 策略：#AIMahjong #MahjongAI #OnlineMahjong #MahjongGame #AIgaming
- 每條 Tweet 包含 2-3 個相關 Hashtag
- Tweet 內容包含「AI Mahjong」「Mahjong with AI」等關鍵詞

### 2.3 Discord 策略

**目標：** 建立忠誠玩家社群，提升用戶留存

| 頻道 | 功能 | 目標成員 |
|------|------|----------|
| **#general** | 玩家吹水 | 無上限 |
| **#ai-arena** | 遊戲討論 | 無上限 |
| **#tournaments** | 比賽資訊 | 無上限 |
| **#bugs-feedback** | 問題回報 | 無上限 |
| **#content-creators** | 内容創作者專區 | 100+ |
| **#dev-updates** | 開發者更新日 | 無上限 |

**Discord 病毒式增長策略：**
- 邀請獎勵：邀請 3 人入群 → 獲得 exclusive avatar
- 每日挑戰：Discord 內完成每日任務 → 獎勵遊戲內金幣
- 專屬賽事：Discord 玩家專屬 tournament

---

## 3. 爆紅切入點 - 點樣 Viral？

### 3.1 病毒式增長既底層邏輯

> **核心洞察：** 要 Viral，必須創造「值得分享既時刻」(Shareable Moment)

### 3.2 五大 Viral 切入點

#### 切入點 1：AI 戰勝人類既戲劇性時刻 🎯

**策略：** 製造 AI 擊敗知名玩家既話題

| 行動 | 描述 |
|------|------|
| **挑戰知名玩家** | 邀請麻雀冠軍、實況主與 AI 對戰 |
| **紀錄片風格** | 拍攝「人類 vs AI」紀錄片 |
| **情緒共鳴** | 「AI 居然做到呢一步」既震驚感 |

**案例參考：** AlphaGo vs 李世石 - 呢個就係最经典既 AI vs 人類敘事

#### 切入點 2：社交分享優化 (Shareability) 🎯

**策略：** 設計「分享獎勵」機制

| 功能 | 描述 |
|------|------|
| **精彩片段分享** | 一鍵分享 AI 精華對局到 Twitter/Discord |
| **戰績海報** | 自動生成靚既戰績圖片，分享到社交媒體 |
| **排行榜炫耀** | 「我既排名係全球 Top 100」分享功能 |
| **挑戰朋友** | 邀請朋友对战既專屬連結 |

#### 切入點 3：獵奇 + 教育內容 🎯

**策略：** 用 AI 既「未知性」吸引流量

| 內容 | 描述 |
|------|------|
| **「AI 居然咁樣打？」** | AI 奇怪但正確既打法展示 |
| **AI 策略分析** | 「AI 教你點樣提升麻雀技術」教學系列 |
| **AI 心理學** | 「AI 點樣讀懂你既心理」科普內容 |

#### 切入點 4：時事/熱點借勢 🎯

**策略：** 緊貼 AI 熱潮，借勢推廣

| 時機 | 行動 |
|------|------|
| **ChatGPT 新版本發布** | 「我地既 AI 麻雀都用最新 GPT 模型」 |
| **AI 新聞熱話** | 及時發佈相關內容，搶佔流量 |
| **節日推廣** | 農曆新年 - 傳統麻雀 vs AI 麻雀 |

#### 切入點 5：KOL/Influencer 合作 🎯

**策略：** 借助他人流量

| KOL 類型 | 目標 | 預期效果 |
|----------|------|----------|
| **麻雀 YouTuber** | 10-50K 訂閱 | 遊戲推廣 + 合法性背書 |
| **AI 科技頻道** | 50K+ 訂閱 | 「AI + 遊戲」跨界曝光 |
| **遊戲實況主** | 20K+ 觀眾 | 即時流量 + 玩家轉化 |
| **Twitter AI KOL** | 10K+ 粉絲 | 科技圈曝光 |

---

## 4. 競爭對手分析 - 其他 AI 麻雀

### 4.1 市場上既 AI 麻雀遊戲

| 遊戲名稱 | 平台 | AI 功能 | 市場位置 | 弱點 |
|----------|------|---------|----------|------|
| **Mahjong Soul** | Web/Mobile | 基礎 AI | 日本/全球 | AI 較弱、無創新 |
| **Mahjong Titans** | Web | 簡單 AI | 休閒玩家 | 功能單一 |
| **Tencent Mahjong** | Mobile | 強 AI | 中國 | 需要中國手機號 |
| **Yahoo! Mahjong** | Web | 一般 AI | 日本 | 缺乏新意 |
| **Ai-Mahjong (新興)** | Web | GPT-based | 實驗階段 | 功能不成熟 |

### 4.2 競爭對手營銷策略分析

| 對手 | 主要營銷渠道 | 優勢 | 我地既應對 |
|------|--------------|------|------------|
| **Mahjong Soul** | Google Ads、Twitter | 品牌成熟、玩家基礎大 | 差異化：AI 技術領先 |
| **Tencent** | 內置流量、微信推廣 | 用戶量大、資源充足 | 差異化：全球化、獨立平台 |
| **小型 AI 麻雀** | Reddit、Discord | 社群驅動 | 差異化：專業 AI + 內容營銷 |

### 4.3 我地既 Unique Selling Proposition (USP)

| USP | 描述 | 對手缺乏 |
|-----|------|----------|
| **Advanced AI** | 使用最新 LLM 模型，AI 决策更智能 | ⭐⭐⭐⭐⭐ |
| **Global Accessible** | 全球化平台，無地域限制 | ⭐⭐⭐⭐ |
| **Social First** | 社交分享、對戰功能優先 | ⭐⭐⭐ |
| **Content Driven** | AI 教學、策略內容輸出 | ⭐⭐⭐⭐⭐ |
| **Freemium** | 免費版本可用，付費解鎖進階 | ⭐⭐⭐⭐ |

---

## 5. 總結與下一步

### 5.1 關鍵行動項目 (OKR)

| Objective | Key Results | Owner |
|-----------|-------------|-------|
| **AI SEO 權威建立** | Week 8 前完成所有技術優化 + 50+ 文章發佈 | COO |
| **社交媒體啟動** | YouTube/Twitter/Discord 帳號建立並發佈內容 | CMO (外判) |
| **Viral 測試** | 2 個 Viral 切入點測試並驗證效果 | COO |
| **KOL 合作** | 聯繫 5 位潛在 KOL，達成 1-2 個合作 | COO |

### 5.2 預算估算

| 項目 | 預算範圍 (HKD) | 優先度 |
|------|----------------|--------|
| **內容創作** | $5,000-10,000/月 | 🔴 P0 |
| **KOL 合作** | $10,000-30,000/次 | 🔴 P0 |
| **廣告投放** | $5,000-20,000/月 | 🟡 P1 |
| **工具訂閱** | $1,000-3,000/月 | 🟡 P1 |

### 5.3 風險與緩解

| 風險 | 影響 | 緩解措施 |
|------|------|----------|
| **AI 搜尋算法變化** | 高 | 持續監控、多元化流量來源 |
| **競爭對手快速跟進** | 中 | 保持技術領先、建立用戶忠誠度 |
| **社交平台政策變化** | 中 | 多平台佈局、不依賴單一渠道 |

---

## 📊 Think Aloud 總結

**我既假設係：**
- 要做到「AI 提到既麻雀遊戲」，核心在於建立內容權威 + 結構化數據
- Viral 既關鍵係「情緒共鳴」+「社交貨幣」
- 競爭對手多但缺乏「AI 技術領先 + 內容營銷」既玩家

**驗證方法：**
- 發佈內容後監控 AI 平台搜尋結果排名
- 追蹤社交媒體既 engagement metrics
- 定期評估 KOL 合作既 ROI

---

**交付狀態：** ✅ Phase 1 市場研究完成

**下一步：** 需要 CEO 批准進入 Phase 2 (數據建模與設計)

---

*[COO_SIGNED_2026_03_10_0125_HKT]*
*[BOSS_APPROVED_YYYY_MM_DD]*

