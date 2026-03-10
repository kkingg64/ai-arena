"""
WebSocket 連接管理器
"""
import json
from typing import Dict, List
from fastapi import WebSocket
import logging

logger = logging.getLogger(__name__)


class ConnectionManager:
    """WebSocket 連接管理器"""
    
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}
    
    async def connect(self, websocket: WebSocket, game_id: str):
        """客戶端連接"""
        await websocket.accept()
        if game_id not in self.active_connections:
            self.active_connections[game_id] = []
        self.active_connections[game_id].append(websocket)
        logger.info(f"Client connected to game {game_id}")
    
    def disconnect(self, websocket: WebSocket, game_id: str):
        """客戶端斷開"""
        if game_id in self.active_connections:
            if websocket in self.active_connections[game_id]:
                self.active_connections[game_id].remove(websocket)
            if not self.active_connections[game_id]:
                del self.active_connections[game_id]
        logger.info(f"Client disconnected from game {game_id}")
    
    async def send_message(self, websocket: WebSocket, message: dict):
        """發送訊息到單個客戶端"""
        try:
            await websocket.send_json(message)
        except Exception as e:
            logger.error(f"Error sending message: {e}")
    
    async def broadcast(self, game_id: str, message: dict):
        """廣播訊息到所有客戶端"""
        if game_id not in self.active_connections:
            return
        
        disconnected = []
        for connection in self.active_connections[game_id]:
            try:
                await connection.send_json(message)
            except Exception as e:
                logger.error(f"Error broadcasting: {e}")
                disconnected.append(connection)
        
        # 清理斷開的連接
        for ws in disconnected:
            self.disconnect(ws, game_id)
    
    async def broadcast_game_state(self, game_id: str, game_state: dict):
        """廣播遊戲狀態"""
        message = {
            "type": "game_state",
            "game_id": game_id,
            "timestamp": "2026-03-10T00:00:00Z",
            "data": game_state
        }
        await self.broadcast(game_id, message)
    
    async def broadcast_ai_thinking(self, game_id: str, player_id: str, player_name: str, thinking: str):
        """廣播 AI 思考中"""
        message = {
            "type": "ai_thinking",
            "game_id": game_id,
            "timestamp": "2026-03-10T00:00:00Z",
            "data": {
                "player_id": player_id,
                "player_name": player_name,
                "thinking": thinking
            }
        }
        await self.broadcast(game_id, message)
    
    async def broadcast_ai_decision(self, game_id: str, player_id: str, player_name: str, 
                                     action: str, tile: str = None, reasoning: str = ""):
        """廣播 AI 決定"""
        message = {
            "type": "ai_decision",
            "game_id": game_id,
            "timestamp": "2026-03-10T00:00:00Z",
            "data": {
                "player_id": player_id,
                "player_name": player_name,
                "action": action,
                "tile": tile,
                "reasoning": reasoning
            }
        }
        await self.broadcast(game_id, message)
    
    async def broadcast_tile_discarded(self, game_id: str, player_id: str, tile: str):
        """廣播打牌"""
        message = {
            "type": "tile_discarded",
            "game_id": game_id,
            "timestamp": "2026-03-10T00:00:00Z",
            "data": {
                "player_id": player_id,
                "tile": tile,
                "animation": {
                    "from": "hand",
                    "to": "river",
                    "duration_ms": 500,
                    "path": "arc"
                }
            }
        }
        await self.broadcast(game_id, message)
    
    async def broadcast_action(self, game_id: str, action_type: str, player_id: str, data: dict = None):
        """廣播動作"""
        message = {
            "type": action_type,
            "game_id": game_id,
            "timestamp": "2026-03-10T00:00:00Z",
            "data": {
                "player_id": player_id,
                **(data or {})
            }
        }
        await self.broadcast(game_id, message)
    
    async def broadcast_error(self, game_id: str, error: str):
        """廣播錯誤"""
        message = {
            "type": "error",
            "game_id": game_id,
            "timestamp": "2026-03-10T00:00:00Z",
            "data": {
                "error": error
            }
        }
        await self.broadcast(game_id, message)


# 全局連接管理器實例
manager = ConnectionManager()
