import pandas as pd

from config import DatabaseSettings, PathsSettings
database_settings = DatabaseSettings()
# database_settings = DatabaseSettings(_env_file='.env.dev')
paths_settings = PathsSettings()

df = pd.read_csv(paths_settings.RAW_DATA_DIR / 'client.csv')

if __name__ == '__main__':
    print(f'PG HOST: {database_settings.PG_HOST}')
    print(f'PG PORT: {database_settings.PG_PORT}')
    #print(f'PG PASSWORD: {database_settings.PG_PASSWORD}')
    #print(f'PG PASSWORD: {database_settings.PG_PASSWORD.get_secret_value()}')
    print(f'PG DSN: {database_settings.PG_DSN}')
    print(f'VARVAR: {database_settings.VARVAR}')
    print(f'RAW_DATA_DIR: {paths_settings.RAW_DATA_DIR}')
    print(f'df: {df}')