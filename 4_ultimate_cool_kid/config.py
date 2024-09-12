from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    PROJECT_DIR: Path = Path(__file__).parent.resolve()
    model_config = SettingsConfigDict(env_file=PROJECT_DIR / ".env", extra="ignore")

    PG_HOST: str = 'localhost'
    PG_PORT: int = 8080
    PG_PASSWORD: SecretStr


class PathsSettings(BaseSettings):
    PROJECT_DIR: Path = Path(__file__).parent.resolve()
    model_config = SettingsConfigDict(env_file=PROJECT_DIR / ".env", extra="ignore")

    RAW_DATA_DIR: Path = Path(PROJECT_DIR / 'data/raw')
