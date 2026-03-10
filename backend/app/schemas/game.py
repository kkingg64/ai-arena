from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class TileSuit(str, Enum):
    WAN = "W"      # 萬子
    TONG = "D"     # 筒子
    TIAO = "S"     # 索子
    ZI = "Z"       # 字牌
    FLOWER = "F"   # 花牌
    SEASON = "K"   # 季節


class ActionType(str, Enum):
    DISCARD = "discard"
    PON = "pon"
    KONG = "kong"
    RON = "ron"
    ZIMO = "zimo"
    SKIP = "skip"


class MessageType(str, Enum):
    GAME_STATE = "game_state"
    PLAYER_ACTION = "player_action"
    AI_THINKING = "ai_thinking"
    AI_DECISION = "ai_decision"
    TILE_DRAWN = "tile_drawn"
    TILE_DISCARDED = "tile_discarded"
    PON = "pon"
    KONG = "kong"
    RON = "ron"
    ZIMO = "zimo"
    GAME_OVER = "game_over"
    ERROR = "error"


# ============ Schemas ============

class Tile(BaseModel):
    """麻雀牌"""
    id: str  # e.g., "1W", "2D", "5Z"


class Meld(BaseModel):
    """面子 (吃/碰/槓)"""
    type: str  # "chow", "pon", "kong"
    tiles: List[str]
    from_player: Optional[int] = None  # 從邊個玩家吃/碰


class PlayerState(BaseModel):
    """玩家狀態"""
    player_id: str
    seat: int
    name: str
    hand: List[str] = []
    discards: List[str] = []
    melds: List[Meld] = []
    riichi: bool = False
    points: int = 25000
    available_actions: List[str] = []


class GameConfig(BaseModel):
    """遊戲配置"""
    debug: bool = False
    model_a: str = "gpt4o"
    model_b: str = "claude"
    model_c: str = "gemini"
    model_d: str = "llama"


class GameCreateRequest(BaseModel):
    """創建遊戲請求"""
    players: List[str]  # 模型類型列表
    config: Optional[GameConfig] = None


class GameResponse(BaseModel):
    """遊戲響應"""
    game_id: str
    status: str
    players: List[dict] = []


class PlayerAction(BaseModel):
    """玩家動作"""
    player_id: str
    action: str
    tile: Optional[str] = None


class GameStateResponse(BaseModel):
    """遊戲狀態響應"""
    game_id: str
    round: int
    wind: str
    dealer: int
    current_player: int
    players: List[PlayerState]
    last_action: Optional[dict] = None
    pending_actions: Optional[dict] = None
    game_status: str


class WSMessage(BaseModel):
    """WebSocket 訊息"""
    type: MessageType
    game_id: str
    timestamp: str
    data: dict
