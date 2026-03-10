"""
廣東麻雀裁判伺服器 (The Umpire)
負責：洗牌、發牌、碰/槓/胡判定、番數計算
"""
import random
import uuid
from typing import List, Optional, Dict, Tuple
from dataclasses import dataclass, field
from enum import Enum


class TileSuit(str, Enum):
    WAN = "W"      # 萬子
    TONG = "D"     # 筒子
    TIAO = "S"     # 索子
    ZI = "Z"       # 字牌
    FLOWER = "F"   # 花牌
    SEASON = "K"   # 季節


# ============ 麻雀牌定義 (144張) ============

# 數字牌 (36種 x 4 = 144張，但實際只有 9+9+9=27種 x 4 = 108張)
NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
SUITS = ["W", "D", "S"]  # 萬、筒、索

# 字牌 (7種 x 4 = 28張)
HONORS = ["1Z", "2Z", "3Z", "4Z", "5Z", "6Z", "7Z"]  # 東南西北中發白

# 花牌 (4張)
FLOWERS = ["1F", "2F", "3F", "4F"]  # 梅、蘭、菊、竹

# 季節 (4張)
SEASONS = ["1K", "2K", "3K", "4K"]  # 春、夏、秋、冬


def generate_all_tiles() -> List[str]:
    """生成完整既麻雀牌組 (144張)
    
    麻雀牌組成：
    - 萬子牌 (1-9) x 4 = 36張
    - 筒子牌 (1-9) x 4 = 36張
    - 索子牌 (1-9) x 4 = 36張
    - 字牌 (東/南/西/北/中/發/白) x 4 = 28張
    - 花牌 (梅/蘭/菊/竹) x 1 = 4張
    - 季節 (春/夏/秋/冬) x 1 = 4張
    
    總共：144張
    """
    tiles = []
    
    # 數字牌：9種 x 3套花色 x 4張 = 108張
    for suit in SUITS:
        for num in NUMBERS:
            for _ in range(4):
                tiles.append(f"{num}{suit}")
    
    # 字牌：7種 x 4張 = 28張
    for honor in HONORS:
        for _ in range(4):
            tiles.append(honor)
    
    # 花牌：8張 (每隻1張)
    tiles.extend(FLOWERS)
    
    # 季節：4張 (每隻1張)
    tiles.extend(SEASONS)
    
    assert len(tiles) == 144, f"Should be 144 tiles, got {len(tiles)}"
    return tiles


def generate_standard_tiles() -> List[str]:
    """標準麻雀牌 (136張 - 去掉花牌) 或 (144張 - 完整)"""
    tiles = []
    
    # 數字牌：9 x 3 x 4 = 108
    for suit in SUITS:
        for num in NUMBERS:
            tiles.extend([f"{num}{suit}"] * 4)
    
    # 字牌：7 x 4 = 28
    for h in HONORS:
        tiles.extend([h] * 4)
    
    # 花牌季節 (可選)
    # tiles.extend(FLOWERS)   # +8
    # tiles.extend(SEASONS)   # +4
    
    return tiles  # 136張標準麻雀


# ============ 番數計算器 ============

class MahjongScorer:
    """廣東麻雀番數計算器"""
    
    # 番數表
    FAN_TABLE = {
        # 牌型 (3-10番)
        "duidui": 3,           # 對對糊
        "hunyise": 3,          # 混一色
        "qingyise": 7,         # 清一色
        "xiaosanyuan": 5,      # 小三元
        "dasanyuan": 8,        # 大三元
        "xiaosixi": 6,         # 小四喜
        "dasixi": 10,          # 大四喜
        "kehe": 8,             # 刻刻糊
        "ziyise": 10,          # 字一色
        "qingyijiu": 10,       # 清么九
        "shisanyao": 10,       # 十三么
        "shibaluohan": 10,     # 十八羅漢
        "jiuzilianhuan": 10,  # 九字連環
        
        # 糊牌 (1番)
        "zimo": 1,             # 自摸
        "gangshang": 1,        # 槓上自摸
        "haidilaoyue": 1,      # 海底撈月
        "qianggang": 1,        # 搶槓
        "menqianqing": 1,      # 門前清
        "pinghu": 1,           # 平糊
        "huayau": 1,           # 花么
        
        # 番子 (1番)
        "sanyuan": 1,          # 三元牌
        "quanjia": 1,          # 圈風
        "menfeng": 1,          # 門風
    }
    
    # 番數積分表
    FAN_POINTS_TABLE = {
        3: {"zimo": 24, "rong": 16},
        4: {"zimo": 48, "rong": 32},
        5: {"zimo": 72, "rong": 48},
        6: {"zimo": 96, "rong": 64},
        7: {"zimo": 144, "rong": 96},
        8: {"zimo": 192, "rong": 128},
        9: {"zimo": 288, "rong": 192},
        10: {"zimo": 384, "rong": 256},
    }
    
    MIN_FAN = 3
    MAX_FAN = 10
    
    @classmethod
    def is_number_tile(cls, tile: str) -> bool:
        """判斷是否數字牌"""
        return tile[1] in ["W", "D", "S"]
    
    @classmethod
    def is_honor_tile(cls, tile: str) -> bool:
        """判斷是否字牌"""
        return tile[1] == "Z"
    
    @classmethod
    def is_terminal(cls, tile: str) -> bool:
        """判斷是否么九牌 (1或9)"""
        return tile[0] in ["1", "9"]
    
    @classmethod
    def get_tile_suit(cls, tile: str) -> str:
        """獲取牌既花色"""
        if len(tile) == 2:
            return tile[1]
        return tile[1]
    
    @classmethod
    def count_sets(cls, hand: List[str]) -> Tuple[int, List[str]]:
        """計算牌組 (面子 + 對眼)
        返回: (面子數, 餘牌)
        """
        # 簡化版：檢查標準胡牌型 (4面子 + 1對)
        return cls._check_win_pattern(hand)
    
    @classmethod
    def _check_win_pattern(cls, hand: List[str]) -> Tuple[int, List[str]]:
        """檢查胡牌型"""
        if len(hand) != 14:
            return 0, hand
        
        # 嘗試找對子
        for i in range(len(hand)):
            pair = hand[i]
            remaining = hand[:i] + hand[i+1:]
            
            # 檢查剩餘13張是否可以分成4組順子/刻子
            if cls._can_form_sets(remaining):
                return 4, [pair]
        
        return 0, hand
    
    @classmethod
    def _can_form_sets(cls, tiles: List[str]) -> bool:
        """檢查是否可以將牌分成順子或刻子"""
        if not tiles:
            return True
        
        if len(tiles) % 3 != 0:
            return False
        
        # 取出第一張牌，嘗試組成刻子或順子
        first = tiles[0]
        
        # 1. 嘗試刻子 (3張相同)
        count = tiles.count(first)
        if count >= 3:
            new_tiles = tiles.copy()
            for _ in range(3):
                new_tiles.remove(first)
            if cls._can_form_sets(new_tiles):
                return True
        
        # 2. 嘗試順子 (僅限數字牌)
        if cls.is_number_tile(first):
            suit = first[1]
            num = int(first[0])
            
            # 嘗試吃上家
            next_tile = f"{num+1}{suit}"
            next_next = f"{num+2}{suit}"
            
            if next_tile in tiles and next_next in tiles:
                new_tiles = tiles.copy()
                new_tiles.remove(first)
                new_tiles.remove(next_tile)
                new_tiles.remove(next_next)
                if cls._can_form_sets(new_tiles):
                    return True
        
        return False
    
    @classmethod
    def calculate_fan(cls, hand: List[str], melds: List[Dict], 
                       is_zimo: bool, flowers: int,
                       has_menqianqing: bool = False,
                       has_pinghu: bool = False,
                       has_qingyise: bool = False,
                       has_hunyise: bool = False,
                       has_duidui: bool = False) -> int:
        """計算總番數"""
        total_fan = 0
        
        # 花牌
        total_fan += min(flowers, 10)
        
        # 糊牌
        if is_zimo:
            total_fan += 1
        if has_menqianqing:
            total_fan += 1
        if has_pinghu:
            total_fan += 1
        
        # 牌型
        if has_qingyise:
            total_fan += 7
        if has_hunyise:
            total_fan += 3
        if has_duidui:
            total_fan += 3
        
        return min(total_fan, cls.MAX_FAN)
    
    @classmethod
    def calculate_points(cls, fan: int, is_zimo: bool, base_points: int = 1000) -> int:
        """計算積分"""
        if fan < cls.MIN_FAN:
            return 0
        
        capped_fan = min(fan, cls.MAX_FAN)
        
        if capped_fan in cls.FAN_POINTS_TABLE:
            points = cls.FAN_POINTS_TABLE[capped_fan]["zimo" if is_zimo else "rong"]
            return points * (base_points // 1000)
        
        return 0


# ============ 裁判伺服器 (The Umpire) ============

@dataclass
class Player:
    """玩家狀態"""
    player_id: str
    seat: int
    name: str
    hand: List[str] = field(default_factory=list)
    discards: List[str] = field(default_factory=list)
    melds: List[Dict] = field(default_factory=list)  # [{"type": "pon/kong", "tiles": [...]}]
    riichi: bool = False
    points: int = 25000
    available_actions: List[str] = field(default_factory=list)
    flowers: List[str] = field(default_factory=list)


@dataclass
class GameState:
    """遊戲狀態"""
    game_id: str
    round: int = 1
    wind: str = "East"  # East, South, West, North
    dealer: int = 0  # 莊家座位
    
    wall: List[str] = field(default_factory=list)  # 牌牆
    wall_index: int = 0  # 當前抽牌位置
    dead_wall: List[str] = field(default_factory=list)  # 死牌
    dora_indicators: List[str] = field(default_factory=list)  # 寶牌指示
    
    players: List[Player] = field(default_factory=list)
    current_player: int = 0  # 當前行動玩家
    last_action: Optional[Dict] = None
    
    pending_actions: Optional[Dict] = None  # 等待其他玩家回應
    game_status: str = "waiting"  # waiting, playing, round_end, game_end
    
    # Debug mode
    debug: bool = False


class MahjongUmpire:
    """廣東麻雀裁判"""
    
    def __init__(self, debug: bool = False):
        self.debug = debug
        self.games: Dict[str, GameState] = {}
        self.scorer = MahjongScorer()
    
    def create_game(self, game_id: str, player_names: List[str], debug: bool = False) -> GameState:
        """創建新遊戲"""
        state = GameState(
            game_id=game_id,
            debug=debug
        )
        
        # 創建玩家
        for i, name in enumerate(player_names):
            state.players.append(Player(
                player_id=f"ai-{name.lower().replace(' ', '-')}-{i:03d}",
                seat=i,
                name=name
            ))
        
        # 初始化遊戲
        self._initialize_round(state)
        
        self.games[game_id] = state
        return state
    
    def _initialize_round(self, state: GameState):
        """初始化回合 (洗牌發牌)"""
        # 生成牌 (144張完整麻雀牌)
        tiles = generate_all_tiles()
        
        if self.debug:
            # Debug mode: 固定牌序方便測試
            random.seed(42)
        
        random.shuffle(tiles)
        state.wall = tiles
        state.wall_index = 0
        
        # 設定死牌 (最後14張)
        state.dead_wall = state.wall[-14:]
        state.wall = state.wall[:-14]
        
        # 莊家摸牌 (14張)，其他13張
        for i, player in enumerate(state.players):
            if i == state.dealer:
                player.hand = state.wall[state.wall_index:state.wall_index+14]
                state.wall_index += 14
            else:
                player.hand = state.wall[state.wall_index:state.wall_index+13]
                state.wall_index += 13
        
        # 翻開寶牌指示
        state.dora_indicators = [state.dead_wall[0]]
        
        # 設定當前玩家為莊家
        state.current_player = state.dealer
        state.game_status = "playing"
        
        # 檢查可用動作
        self._update_available_actions(state)
    
    def _update_available_actions(self, state: GameState):
        """更新玩家可用動作"""
        player = state.players[state.current_player]
        player.available_actions = ["discard"]
        
        # 檢查是否可以碰/槓/胡
        if state.last_action and state.last_action["action"] == "discard":
            discard_tile = state.last_action["tile"]
            from_player = state.last_action["player"]
            
            # 碰
            if player.hand.count(discard_tile) >= 2:
                player.available_actions.append("pon")
            
            # 槓
            if player.hand.count(discard_tile) >= 3:
                player.available_actions.append("kong")
            
            # 食胡 (他人打出的牌)
            if self._can_win(player.hand + [discard_tile], player.melds):
                player.available_actions.append("ron")
        
        # 自摸檢查 (每次摸牌後)
        # 檢查摸到的牌是否可以自摸
        if len(player.hand) == 14:  # 摸牌後
            if self._can_win(player.hand, player.melds):
                player.available_actions.append("zimo")
    
    def draw_tile(self, state: GameState, player_index: int) -> Optional[str]:
        """玩家摸牌"""
        if state.wall_index >= len(state.wall):
            return None  # 荒牌
        
        player = state.players[player_index]
        tile = state.wall[state.wall_index]
        state.wall_index += 1
        
        player.hand.append(tile)
        
        # 檢查花牌
        if tile in FLOWERS or tile in SEASONS:
            player.flowers.append(tile)
            # 摸到花可以再摸一張
            return self.draw_tile(state, player_index)
        
        return tile
    
    def discard_tile(self, state: GameState, player_index: int, tile: str) -> bool:
        """玩家打牌"""
        player = state.players[player_index]
        
        if tile not in player.hand:
            return False
        
        player.hand.remove(tile)
        player.discards.append(tile)
        
        state.last_action = {
            "player": player_index,
            "action": "discard",
            "tile": tile
        }
        
        # 檢查其他玩家是否可行動作
        self._check_pending_actions(state, tile, player_index)
        
        return True
    
    def _check_pending_actions(self, state: GameState, tile: str, from_player: int):
        """檢查其他玩家是否可碰/槓/胡"""
        pending = []
        
        for i, player in enumerate(state.players):
            if i == from_player:
                continue
            
            player.available_actions = []
            
            # 碰
            if player.hand.count(tile) >= 2:
                pending.append({
                    "player": i,
                    "actions": ["pon", "skip"],
                    "from_player": from_player,
                    "tile": tile
                })
                player.available_actions = ["pon", "skip"]
            
            # 槓
            elif player.hand.count(tile) >= 3:
                pending.append({
                    "player": i,
                    "actions": ["kong", "skip"],
                    "from_player": from_player,
                    "tile": tile
                })
                player.available_actions = ["kong", "skip"]
            
            # 食胡
            if self._can_win(player.hand + [tile], player.melds):
                if "ron" not in player.available_actions:
                    player.available_actions.append("ron")
        
        if pending:
            state.pending_actions = pending[0]  # 按座位順序
            state.game_status = "pending"
        else:
            # 下一家
            state.current_player = (from_player + 1) % 4
            self._update_available_actions(state)
    
    def pon(self, state: GameState, player_index: int, tile: str) -> bool:
        """碰"""
        player = state.players[player_index]
        
        if "pon" not in player.available_actions:
            return False
        
        # 移除手牌
        for _ in range(2):
            player.hand.remove(tile)
        
        # 加上碰牌
        player.melds.append({
            "type": "pon",
            "tiles": [tile, tile, tile],
            "from_player": state.last_action["player"]
        })
        
        state.last_action = {
            "player": player_index,
            "action": "pon",
            "tile": tile
        }
        
        state.pending_actions = None
        state.current_player = player_index
        
        # 碰後可打牌
        self._update_available_actions(state)
        
        return True
    
    def kong(self, state: GameState, player_index: int, tile: str) -> bool:
        """槓"""
        player = state.players[player_index]
        
        if "kong" not in player.available_actions:
            return False
        
        # 明槓 (碰後槓) 或 暗槓
        if player.hand.count(tile) >= 4:
            # 暗槓
            for _ in range(4):
                player.hand.remove(tile)
            player.melds.append({
                "type": "kong",
                "tiles": [tile, tile, tile, tile]
            })
        else:
            # 明槓
            for _ in range(3):
                player.hand.remove(tile)
            player.melds.append({
                "type": "kong",
                "tiles": [tile, tile, tile, tile],
                "from_player": state.last_action["player"]
            })
        
        # 槓後摸牌
        drawn = self.draw_tile(state, player_index)
        if drawn:
            # 檢查槓上自摸
            if self._can_win(player.hand, player.melds):
                player.available_actions = ["discard", "zimo"]
            else:
                player.available_actions = ["discard"]
        
        state.last_action = {
            "player": player_index,
            "action": "kong",
            "tile": tile
        }
        
        state.pending_actions = None
        return True
    
    def ron(self, state: GameState, player_index: int) -> bool:
        """食胡 (他人打出的牌)"""
        player = state.players[player_index]
        
        if "ron" not in player.available_actions:
            return False
        
        # 加上別人打的牌
        tile = state.last_action["tile"]
        player.hand.append(tile)
        
        # 計算番數
        fan = self.scorer.calculate_fan(
            player.hand,
            player.melds,
            is_zimo=False,
            flowers=len(player.flowers),
            has_menqianqing=len(player.melds) == 0
        )
        
        if fan >= self.scorer.MIN_FAN:
            points = self.scorer.calculate_points(fan, False)
            
            # 遊戲結束
            state.game_status = "game_end"
            state.winner_id = player.player_id
            
            return True
        
        return False
    
    def zimo(self, state: GameState, player_index: int) -> bool:
        """自摸"""
        player = state.players[player_index]
        
        if "zimo" not in player.available_actions:
            return False
        
        # 計算番數
        fan = self.scorer.calculate_fan(
            player.hand,
            player.melds,
            is_zimo=True,
            flowers=len(player.flowers),
            has_menqianqing=len(player.melds) == 0
        )
        
        if fan >= self.scorer.MIN_FAN:
            points = self.scorer.calculate_points(fan, True)
            
            # 遊戲結束
            state.game_status = "game_end"
            state.winner_id = player.player_id
            
            return True
        
        return False
    
    def _can_win(self, hand: List[str], melds: List[Dict]) -> bool:
        """檢查是否胡牌"""
        # 簡化版：只檢查標準4面子+1對
        return self.scorer._can_form_sets(hand[:-1])  # 去掉摸到的牌
    
    def get_state(self, game_id: str) -> Optional[GameState]:
        """獲取遊戲狀態"""
        return self.games.get(game_id)
    
    def to_dict(self, state: GameState) -> Dict:
        """轉換為可序列化字典"""
        return {
            "game_id": state.game_id,
            "round": state.round,
            "wind": state.wind,
            "dealer": state.dealer,
            "wall_remaining": len(state.wall) - state.wall_index,
            "dead_wall": state.dead_wall,
            "dora_indicators": state.dora_indicators,
            "current_player": state.current_player,
            "players": [
                {
                    "player_id": p.player_id,
                    "seat": p.seat,
                    "name": p.name,
                    "hand": p.hand,
                    "discards": p.discards,
                    "melds": p.melds,
                    "riichi": p.riichi,
                    "points": p.points,
                    "available_actions": p.available_actions,
                    "flowers": p.flowers
                }
                for p in state.players
            ],
            "last_action": state.last_action,
            "pending_actions": state.pending_actions,
            "game_status": state.game_status
        }
