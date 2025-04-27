import os
import secrets
from typing import List, Dict, Any, Optional
from pydantic import field_validator, AnyUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables with defaults.
    
    Includes database configuration, API settings, security settings,
    and other application-specific configuration.
    """
    # API configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "ElementSim"
    
    # CORS settings
    CORS_ORIGINS: List[str] = ["*"]
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", secrets.token_urlsafe(32))
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # Database
    POSTGRES_SERVER: Optional[str] = os.getenv("POSTGRES_SERVER")
    POSTGRES_USER: Optional[str] = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: Optional[str] = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB: Optional[str] = os.getenv("POSTGRES_DB", "element_sim")
    POSTGRES_PORT: Optional[str] = os.getenv("POSTGRES_PORT", "5432")
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")
    
    # Default to SQLite for development if no PostgreSQL config is provided
    @field_validator("DATABASE_URL", mode="before")
    def assemble_db_url(cls, v: Optional[str], info) -> str:
        if v:
            return v
        
        values = info.data
        
        # If PostgreSQL server is defined, use PostgreSQL
        if values.get("POSTGRES_SERVER"):
            return f"postgresql://{values.get('POSTGRES_USER')}:{values.get('POSTGRES_PASSWORD')}@{values.get('POSTGRES_SERVER')}:{values.get('POSTGRES_PORT')}/{values.get('POSTGRES_DB')}"
        
        # Otherwise, use SQLite for development
        sqlite_path = os.path.join(os.getcwd(), "element_sim.db")
        return f"sqlite:///{sqlite_path}"
    
    # SQLite connection arguments (needed for SQLite only)
    @property
    def DATABASE_CONNECT_ARGS(self) -> Dict:
        """
        Generate appropriate connect_args for the database engine.
        
        For SQLite, we need check_same_thread=False.
        For PostgreSQL, we return an empty dict.
        """
        if self.DATABASE_URL and self.DATABASE_URL.startswith("sqlite"):
            return {"check_same_thread": False}
        return {}
    
    # App specific settings
    ELEMENT_DISCOVERY_RATE: float = 0.1  # Chance of discovering new elements
    MAX_CRAFTING_ATTEMPTS: int = 5  # Maximum crafting attempts per session
    
    class Config:
        case_sensitive = True
        env_file = ".env"


# Create settings instance
settings = Settings()