import pandas as pd

from config import Settings
settings = Settings()

df = pd.read_csv(settings.RAW_DATA_DIR / 'client.csv')

if __name__ == '__main__':
    print(f'PG HOST: {settings.PG_HOST}')
    print(f'PG PORT: {settings.PG_PORT}')
    print(f'RAW_DATA_DIR: {settings.RAW_DATA_DIR}')
    print(f'df: {df}')