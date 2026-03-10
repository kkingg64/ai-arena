"""
應用配置 (Application Configuration)
統一使用 MiniMax API
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """應用配置"""
    # App
    app_name: str = "AI Mahjong Arena"
    debug: bool = False
    
    # Database
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/aiarena"
    
    # MiniMax API (統一使用 VPS 本地 API)
    minimax_api_key: str = "fabio-minimax-key-2026"  # VPS 本地 API Key
    minimax_endpoint: str = "http://76.13.215.13:8081/v1"  # VPS MiniMax API
    
    # CORS
    cors_origins: list = ["https://ai-arena.madhorse.cloud", "http://localhost:3000", "http://76.13.215.13", "http://76.13.215.13:80"]
    
    class Config:
        env_file = ".env"
        extra = "allow"


def get_settings() -> Settings:
    """獲取配置"""
    return Settings()


settings = get_settings()
