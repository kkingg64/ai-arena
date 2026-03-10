from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, ARRAY, JSON, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.core.database import Base
import uuid


class AIPlayer(Base):
    """AI 棋手資料表"""
    __tablename__ = "ai_players"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    model_type = Column(String(50), nullable=False)  # gpt4o, claude, gemini, llama, minimax
    api_key_encrypted = Column(String(500), nullable=True)
    config = Column(JSON, default={})
    rating = Column(Integer, default=1500)
    total_games = Column(Integer, default=0)
    wins = Column(Integer, default=0)
    losses = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class Game(Base):
    """對局記錄表"""
    __tablename__ = "games"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    status = Column(String(20), default="waiting")  # waiting, playing, completed
    players = Column(ARRAY(UUID), nullable=False)
    winner_id = Column(UUID, nullable=True)
    scores = Column(JSON, default={})
    config = Column(JSON, default={})
    game_state = Column(JSON, default={})  # 存儲完整遊戲狀態
    started_at = Column(DateTime(timezone=True), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class GameMove(Base):
    """牌譜記錄表"""
    __tablename__ = "game_moves"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    game_id = Column(UUID(as_uuid=True), ForeignKey("games.id"))
    round_num = Column(Integer, default=1)
    player_id = Column(UUID(as_uuid=True), ForeignKey("ai_players.id"))
    action_type = Column(String(20), nullable=False)  # discard, pon, kong, ron, zimo
    tile = Column(String(5), nullable=True)
    previous_hand = Column(JSON, default=[])
    current_hand = Column(JSON, default=[])
    move_num = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class PlayerMatchup(Base):
    """玩家對戰歷史表"""
    __tablename__ = "player_matchups"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    player_a_id = Column(UUID(as_uuid=True), ForeignKey("ai_players.id"))
    player_b_id = Column(UUID(as_uuid=True), ForeignKey("ai_players.id"))
    player_a_wins = Column(Integer, default=0)
    player_b_wins = Column(Integer, default=0)
    total_games = Column(Integer, default=0)
    last_game_id = Column(UUID, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
