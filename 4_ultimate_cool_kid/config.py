from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_DIR: Path = Path(__file__).parent.resolve()
    model_config = SettingsConfigDict(env_file=PROJECT_DIR / ".env", extra="ignore")

    # Connections
    PG_HOST: str = 'localhost'
    PG_PORT: int = 8080

    # Paths
    RAW_DATA_DIR: Path = Path(PROJECT_DIR / 'data/raw')