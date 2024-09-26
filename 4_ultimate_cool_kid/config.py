import json
import os
from pathlib import Path

import boto3
from botocore.exceptions import ClientError
from pydantic import SecretStr, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

secret_name = "AUMA_TEST"
region_name = "us-east-1"


def get_secret():
    # Create a Secrets Manager client
    session = boto3.session.Session(profile_name='saml')
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret = get_secret_value_response['SecretString']

    return json.loads(secret)


SECRET = get_secret()


class DatabaseSettings(BaseSettings):
    PROJECT_DIR: Path = Path(__file__).parent.resolve()
    model_config = SettingsConfigDict(env_file=PROJECT_DIR / ".env", extra="ignore")

    PG_HOST: str = 'localhost'
    PG_PORT: int = 8080
    PG_PASSWORD: SecretStr = SECRET['PGPASSWORD']
    VARVAR: str = os.getenv("VARVAR", "default value")

    PG_DSN: PostgresDsn = 'postgres://user:pass@localhost:5432/foobar'
    # PG_DSN: PostgresDsn = 'postgrlocalhost:5432/foobar'


class PathsSettings(BaseSettings):
    PROJECT_DIR: Path = Path(__file__).parent.resolve()
    model_config = SettingsConfigDict(env_file=PROJECT_DIR / ".env", extra="ignore")

    RAW_DATA_DIR: Path = Path(PROJECT_DIR / 'data/raw')
