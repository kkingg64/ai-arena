"""
模型大腦適配器 (Model Adapters)
統一使用：MiniMax API
"""
import json
import logging
from abc import ABC, abstractmethod
from typing import Dict
import requests

from app.core.config import settings

logger = logging.getLogger(__name__)


class ModelAdapter(ABC):
    """AI 模型適配器基類"""
    
    @abstractmethod
    async def decide(self, game_state: Dict, player_id: str) -> Dict:
        """根據遊戲狀態做出決定"""
        pass
    
    @abstractmethod
    def get_model_name(self) -> str:
        """返回模型名稱"""
        pass
    
    async def initialize(self) -> bool:
        """初始化模型連接"""
        return True


class MiniMaxAdapter(ModelAdapter):
    """MiniMax 適配器 - 統一使用"""
    
    def __init__(self, api_key: str, endpoint: str = "https://api.minimax.chat/v1"):
        self.api_key = api_key
        self.endpoint = endpoint
        self.model = "MiniMax-M2.5"
        self._system_prompt = self._get_system_prompt()
    
    def get_model_name(self) -> str:
        return "MiniMax-M2.5"
    
    def _get_system_prompt(self) -> str:
        return """你係一個專業既廣東麻雀選手。你既目標係透過合理既出牌策略黎贏得比賽。

遊戲規則：
- 4人麻雀，每人13隻牌，莊家14隻
- 目標：湊成4組面子(順子或刻子) + 1對眼
- 3番起胡
- 可以碰、槓、食胡、自摸

策略建議：
1. 留意海內既牌，避免俾人食胡
2. 保持手牌彈性，唔好太快固定牌型
3. 留意寶牌，等機會做大牌
4. 如果冇野好做，優先打冇用既孤張

你既回應必須係 JSON 格式：
{
  "action": "discard",
  "tile": "1W",
  "reasoning": "因為..."
}
"""
    
    async def decide(self, game_state: Dict, player_id: str) -> Dict:
        prompt = self._build_prompt(game_state, player_id)
        
        try:
            response = requests.post(
                f"{self.endpoint}/text/chatcompletion_v2",
                json={
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": self._system_prompt},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 500
                },
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                timeout=30
            )
            
            result = response.json()
            if "choices" in result and len(result["choices"]) > 0:
                return self._parse_response(result["choices"][0]["message"]["content"])
            
            return {"action": "skip", "reasoning": "no response"}
        except Exception as e:
            logger.error(f"MiniMax error: {e}")
            return {"action": "skip", "reasoning": f"error: {e}"}
    
    def _build_prompt(self, game_state: Dict, player_id: str) -> str:
        player = next((p for p in game_state["players"] if p["player_id"] == player_id), None)
        if not player:
            return ""
        
        prompt = f"""你係 {player['name']}，到你行動。

## 遊戲狀態
圈風: {game_state.get('wind', 'East')}
局: {game_state.get('round', 1)}
你既座位: {player['seat']}
你既持分: {player['points']}

## 你既手牌
{', '.join(sorted(player['hand']))}

## 棄牌區
{', '.join(player.get('discards', []))}

## 其他玩家棄牌
"""
        for p in game_state["players"]:
            if p["player_id"] != player_id:
                prompt += f"{p['name']}: {', '.join(p.get('discards', []))}\n"
        
        available = player.get('available_actions', ['discard'])
        prompt += f"""
## 可行動作
{', '.join(available)}

## 最後動作
{game_state.get('last_action', 'None')}

請以 JSON 格式返回你既決定。
"""
        return prompt
    
    def _parse_response(self, response: str) -> Dict:
        try:
            if "```json" in response:
                response = response.split("```json")[1].split("```")[0]
            elif "```" in response:
                response = response.split("```")[1].split("```")[0]
            
            return json.loads(response.strip())
        except:
            return {"action": "skip", "reasoning": "解析失敗"}
    
    def _default_decision(self, game_state: Dict, player_id: str) -> Dict:
        player = next((p for p in game_state["players"] if p["player_id"] == player_id), None)
        if player and player.get('hand'):
            return {"action": "discard", "tile": player['hand'][0], "reasoning": "default"}
        return {"action": "skip"}


# ============ 模型工廠 ============

class ModelFactory:
    """模型工廠 - 統一使用 MiniMax"""
    
    _adapter: 'MiniMaxAdapter' = None
    
    @classmethod
    def get_adapter(cls, name: str = None) -> 'MiniMaxAdapter':
        """獲取 MiniMax 適配器 (使用配置中的 API)"""
        if cls._adapter is None:
            cls._adapter = MiniMaxAdapter(
                api_key=settings.minimax_api_key,
                endpoint=settings.minimax_endpoint
            )
        return cls._adapter
    
    @classmethod
    def clear_cache(cls):
        """清除適配器緩存"""
        cls._adapter = None
