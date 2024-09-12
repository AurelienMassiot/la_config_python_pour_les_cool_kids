import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

pg_host = 'pghost'
pg_port = 'pgport'
df = pd.read_csv('data/raw/client.csv')

if __name__ == '__main__':
    print(f'PG HOST: {pg_host}')
    print(f'PG PORT: {pg_port}')
    print(f'df: {df}')
