from config import config
import pandas as pd

df = pd.read_csv(config['RAW_DATA_DIR'] + '/' + 'client.csv')

if __name__ == '__main__':
    print(f'PG HOST: {config["PG_HOST"]}')
    print(f'PG PORT: {config["PG_PORT"]}')
    print(f'df: {df}')