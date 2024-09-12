import pandas as pd

from config import DatabaseSettings, PathsSettings
database_settings = DatabaseSettings()
paths_settings = PathsSettings()

df = pd.read_csv(paths_settings.RAW_DATA_DIR / 'client.csv')

if __name__ == '__main__':
    print(f'PG HOST: {database_settings.PG_HOST}')
    print(f'PG PORT: {database_settings.PG_PORT}')
    print(f'PG PASSWORD: {database_settings.PG_PASSWORD}')
    print(f'RAW_DATA_DIR: {paths_settings.RAW_DATA_DIR}')
    print(f'df: {df}')