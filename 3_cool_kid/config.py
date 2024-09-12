import os

from dotenv import load_dotenv

load_dotenv()

config = {
    'PG_HOST': os.getenv('PG_HOST'),
    'PG_PORT': os.getenv('PG_PORT'),
    'RAW_DATA_DIR': os.path.abspath("data/raw")
}
