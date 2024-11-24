# настройки
import os
from dotenv import dotenv_values, find_dotenv
from dotenv import load_dotenv
# from sqlalchemy_imageattach.stores.fs import FileSystemStore


# FileSystemStore(
#     path='/home/andrey/ab/fast_api/images',
#     base_url='http://images.yourapp.com/'
# )


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))

# env_cfg = dotenv_values(find_dotenv(raise_error_if_not_found=True))
load_dotenv(os.path.join(BASE_DIR, '.env'))

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
