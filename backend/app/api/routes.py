"""
API 路由
"""
import uuid
import json  # 添加 json import
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
import logging

from app.core.database import get_db
from app.core.config import settings
from app.schemas.game import (
    GameCreateRequest, GameResponse, GameStateResponse, 
    PlayerAction, WSMessage, MessageType
)
from app.services.umpire import MahjongUmpire
from app.services.websocket import manager
from app.services.adapters import ModelFactory

logger = logging.getLogger(__name__)

router = APIRouter()

# 全局裁判實例 - 從 main.py 導入共享實例
# umpire = MahjongUmpire(debug=settings.debug)  # 移除這行，導入共享實例

try:
    from main import umpire
except ImportError:
    # 如果 main.py 未加載，創建臨時實例
    umpire = MahjongUmpire(debug=settings.debug)


@router.get("/api/leaderboard")
async def get_leaderboard():
    """獲取排行榜數據"""
    # 從內存中收集玩家統計數據
    player_stats = {}
    
    # 遍歷所有遊戲，收集玩家數據
    for game_id, state in umpire.games.items():
        if not state or not state.players:
            continue
            
        for player in state.players:
            name = player.name
            if name not in player_stats:
                player_stats[name] = {
                    "name": name,
                    "games": 0,
                    "wins": 0,
                    "points": 0,
                    "player_id": player.player_id
                }
            
            player_stats[name]["games"] += 1
            player_stats[name]["points"] += player.points
            if player.is_winner:
                player_stats[name]["wins"] += 1
    
    # 如果沒有遊戲數據，返回默認排行榜
    if not player_stats:
        player_stats = {
            "AlphaMaster": {"name": "AlphaMaster", "games": 42, "wins": 33, "points": 9850, "player_id": "alpha-1"},
            "DragonSage": {"name": "DragonSage", "games": 38, "wins": 27, "points": 9420, "player_id": "dragon-1"},
            "PhoenixAI": {"name": "PhoenixAI", "games": 35, "wins": 24, "points": 8950, "player_id": "phoenix-1"},
            "TigerKing": {"name": "TigerKing", "games": 40, "wins": 26, "points": 8320, "player_id": "tiger-1"},
            "FoxStrategy": {"name": "FoxStrategy", "games": 36, "wins": 24, "points": 7890, "player_id": "fox-1"},
            "LionMind": {"name": "LionMind", "games": 32, "wins": 23, "points": 7650, "player_id": "lion-1"},
            "PandaAI": {"name": "PandaAI", "games": 34, "wins": 21, "points": 7210, "player_id": "panda-1"},
            "EagleMind": {"name": "EagleMind", "games": 30, "wins": 20, "points": 6980, "player_id": "eagle-1"},
            "WolfAI": {"name": "WolfAI", "games": 28, "wins": 17, "points": 6540, "player_id": "wolf-1"},
            "SnakeAI": {"name": "SnakeAI", "games": 25, "wins": 14, "points": 5890, "player_id": "snake-1"},
        }
    
    # 轉換為列表並排序
    leaderboard = list(player_stats.values())
    leaderboard.sort(key=lambda x: x["points"], reverse=True)
    
    # 添加排名
    for i, player in enumerate(leaderboard):
        player["rank"] = i + 1
        player["winrate"] = round((player["wins"] / player["games"] * 100) if player["games"] > 0 else 0, 1)
    
    return {
        "leaderboard": leaderboard,
        "total_players": len(leaderboard),
        "total_games": sum(p["games"] for p in leaderboard)
    }


@router.get("/api/games")
async def list_games(limit: int = Query(20)):
    """獲取遊戲列表"""
    games_list = []
    
    for game_id, state in umpire.games.items():
        if not state:
            continue
        
        # 提取玩家名稱
        players = [p.name for p in state.players]
        
        # 找出贏家
        winner = None
        for p in state.players:
            if p.is_winner:
                winner = p.name
                break
        
        games_list.append({
            "game_id": game_id,
            "status": state.game_status,
            "players": players,
            "winner": winner,
            "current_round": getattr(state, 'current_round', '東1'),
            "dealer_seat": getattr(state, 'dealer_seat', 0),
            "created_at": getattr(state, 'created_at', None)
        })
    
    # 按創建時間排序（最新的在前）
    games_list.sort(key=lambda x: x.get("created_at", ""), reverse=True)
    
    return {
        "games": games_list[:limit],
        "total": len(games_list)
    }


@router.get("/")
async def root():
    """健康檢查"""
    return {
        "name": "AI Mahjong Arena API",
        "version": "1.0.0",
        "status": "running"
    }


@router.post("/api/games", response_model=GameResponse)
async def create_game(
    request: GameCreateRequest,
    debug: bool = Query(False)
):
    """創建新對局"""
    game_id = str(uuid.uuid4())
    
    # 玩家名稱
    player_names = request.players if request.players else ["GPT-4o", "Claude", "Gemini", "Llama"]
    
    # Debug mode: 全部用 MiniMax
    if debug or settings.debug:
        player_names = ["MiniMax-A", "MiniMax-B", "MiniMax-C", "MiniMax-D"]
    
    # 創建遊戲
    state = umpire.create_game(game_id, player_names, debug or settings.debug)
    
    # 返回完整遊戲狀態
    return {
        "game_id": game_id,
        "status": state.game_status,
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
                "available_actions": p.available_actions
            }
            for p in state.players
        ]
    }


@router.get("/api/games/{game_id}")
async def get_game_state(game_id: str):
    """獲取遊戲狀態"""
    state = umpire.get_state(game_id)
    
    if not state:
        raise HTTPException(status_code=404, detail="Game not found")
    
    return umpire.to_dict(state)


@router.post("/api/games/{game_id}/action")
async def player_action(
    game_id: str,
    action: PlayerAction
):
    """玩家執行動作"""
    state = umpire.get_state(game_id)
    
    if not state:
        raise HTTPException(status_code=404, detail="Game not found")
    
    player_index = None
    for i, p in enumerate(state.players):
        if p.player_id == action.player_id:
            player_index = i
            break
    
    if player_index is None:
        raise HTTPException(status_code=404, detail="Player not found")
    
    result = {"success": False, "message": ""}
    
    if action.action == "discard":
        success = umpire.discard_tile(state, player_index, action.tile)
        result = {"success": success, "message": f"Discarded {action.tile}" if success else "Invalid tile"}
        
    elif action.action == "pon":
        success = umpire.pon(state, player_index, action.tile)
        result = {"success": success, "message": "Ponned" if success else "Cannot pon"}
        
    elif action.action == "kong":
        success = umpire.kong(state, player_index, action.tile)
        result = {"success": success, "message": "Konged" if success else "Cannot kong"}
        
    elif action.action == "ron":
        success = umpire.ron(state, player_index)
        result = {"success": success, "message": "RON! You win!" if success else "Cannot ron"}
        
    elif action.action == "zimo":
        success = umpire.zimo(state, player_index)
        result = {"success": success, "message": "ZIMO! You win!" if success else "Cannot zimo"}
        
    elif action.action == "skip":
        # 跳過，進入下一家
        state.pending_actions = None
        state.current_player = (player_index + 1) % 4
        result = {"success": True, "message": "Skipped"}
    
    # 廣播更新後的遊戲狀態
    await manager.broadcast_game_state(game_id, umpire.to_dict(state))
    
    return result


@router.post("/api/debug/enable")
async def enable_debug_mode():
    """啟用 Debug Mode"""
    settings.debug = True
    umpire.debug = True
    return {"message": "Debug mode enabled"}


@router.post("/api/debug/disable")
async def disable_debug_mode():
    """關閉 Debug Mode"""
    settings.debug = False
    umpire.debug = False
    return {"message": "Debug mode disabled"}


# ============ AI 遊戲循環 ============

@router.post("/api/games/{game_id}/start-ai")
async def start_ai_game_loop(game_id: str):
    """啟動 AI 遊戲循環"""
    import asyncio
    from app.services.adapters import ModelFactory
    
    state = umpire.get_state(game_id)
    if not state:
        raise HTTPException(status_code=404, detail="Game not found")
    
    # 創建後台任務運行 AI 遊戲
    asyncio.create_task(run_ai_turn(game_id))
    
    return {"message": "AI game loop started", "game_id": game_id}


async def run_ai_turn(game_id: str):
    """運行 AI 回合"""
    adapter = ModelFactory.get_adapter()
    state = umpire.games.get(game_id)
    
    if not state:
        return
    
    # 廣播遊戲開始
    await manager.broadcast_action(game_id, "game_start", "system", {"message": "AI 對戰開始！"})
    
    # 初始摸牌 - 莊家多一張
    dealer = state.dealer
    state.current_player = dealer
    drawn = umpire.draw_tile(state, dealer)
    if drawn:
        await manager.broadcast_action(game_id, "tile_drawn", state.players[dealer].player_id, {"tile": drawn})
        # 檢查自摸
        umpire._update_available_actions(state)
    
    while state.game_status == "playing":
        player = state.players[state.current_player]
        
        # 廣播 AI 思考中
        await manager.broadcast_ai_thinking(
            game_id, 
            player.player_id, 
            player.name, 
            "思考中..."
        )
        
        # 等待一段時間 (模擬思考)
        import asyncio
        await asyncio.sleep(1.5)
        
        # 檢查是否有 pending actions (碰/槓/胡)
        if state.pending_actions and state.pending_actions.get("player") == state.current_player:
            # 玩家需要回應碰/槓/胡
            actions = state.pending_actions.get("actions", [])
            tile = state.pending_actions.get("tile")
            
            # 讓 AI 決定
            game_dict = umpire.to_dict(state)
            decision = await adapter.decide(game_dict, player.player_id)
            
            action = decision.get("action", "skip")
            
            if action == "pon" and "pon" in actions:
                umpire.pon(state, state.current_player, tile)
                await manager.broadcast_action(game_id, "pon", player.player_id, {"tile": tile})
            elif action == "kong" and "kong" in actions:
                umpire.kong(state, state.current_player, tile)
                await manager.broadcast_action(game_id, "kong", player.player_id, {"tile": tile})
            elif action == "ron" and "ron" in actions:
                # 胡牌結算
                fan = umpire.scorer.calculate_fan(
                    player.hand + [tile],
                    player.melds,
                    is_zimo=False,
                    flowers=len(player.flowers)
                )
                points = umpire.scorer.calculate_points(fan, False)
                player.points += points
                player.is_winner = True
                state.game_status = "game_end"
                state.winner_id = player.player_id
                
                await manager.broadcast_action(game_id, "ron", player.player_id, {
                    "fan": fan, 
                    "points": points,
                    "hand": player.hand
                })
                break
            else:
                # 跳過
                state.pending_actions = None
                umpire._update_available_actions(state)
                state.current_player = (state.current_player + 1) % 4
        
        else:
            # 正常回合 - 摸牌然後打牌
            drawn = umpire.draw_tile(state, state.current_player)
            if drawn:
                await manager.broadcast_action(game_id, "tile_drawn", player.player_id, {"tile": drawn})
            
            # 檢查是否荒牌
            if state.wall_index >= len(state.wall):
                state.game_status = "round_end"
                await manager.broadcast_action(game_id, "draw", "system", {"message": "荒牌"})
                break
            
            # 更新可用動作
            umpire._update_available_actions(state)
            
            # 檢查自摸
            if "zimo" in player.available_actions:
                fan = umpire.scorer.calculate_fan(
                    player.hand,
                    player.melds,
                    is_zimo=True,
                    flowers=len(player.flowers)
                )
                if fan >= 3:
                    points = umpire.scorer.calculate_points(fan, True)
                    player.points += points
                    player.is_winner = True
                    state.game_status = "game_end"
                    state.winner_id = player.player_id
                    
                    await manager.broadcast_action(game_id, "zimo", player.player_id, {
                        "fan": fan,
                        "points": points,
                        "hand": player.hand
                    })
                    break
            
            # AI 決定打咩牌
            game_dict = umpire.to_dict(state)
            decision = await adapter.decide(game_dict, player.player_id)
            
            action = decision.get("action", "discard")
            tile = decision.get("tile")
            
            if not tile and player.hand:
                tile = player.hand[0]  # Default: 打第一張
            
            if action == "discard" and tile:
                umpire.discard_tile(state, state.current_player, tile)
                await manager.broadcast_tile_discarded(game_id, player.player_id, tile)
                
                # 廣播 AI 決定
                await manager.broadcast_ai_decision(
                    game_id,
                    player.player_id,
                    player.name,
                    action,
                    tile,
                    decision.get("reasoning", "")
                )
        
        # 廣播遊戲狀態
        await manager.broadcast_game_state(game_id, umpire.to_dict(state))
        
        # 等待一段時間
        await asyncio.sleep(0.5)
    
    # 遊戲結束
    if state.game_status == "game_end":
        winner = state.players[state.current_player]
        await manager.broadcast_action(game_id, "game_over", "system", {
            "winner": winner.name,
            "points": winner.points
        })
    
    return


# ============ WebSocket 端點 ============

@router.websocket("/ws/game/{game_id}")
async def game_websocket(websocket: WebSocket, game_id: str):
    """遊戲即時數據流"""
    await manager.connect(websocket, game_id)
    
    try:
        # 發送當前遊戲狀態
        state = umpire.get_state(game_id)
        if state:
            await manager.broadcast_game_state(game_id, umpire.to_dict(state))
        
        # 持續監聽客戶端訊息
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            
            # 處理客戶端訊息
            # 目前支援：ping
            if message.get("type") == "ping":
                await manager.send_message(websocket, {"type": "pong"})
                
    except WebSocketDisconnect:
        manager.disconnect(websocket, game_id)
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        await manager.broadcast_error(game_id, str(e))
        manager.disconnect(websocket, game_id)

