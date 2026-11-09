from dotenv import load_dotenv
import os

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
YANDEX_URL = 'https://ya.ru/'
GET_WEB_ELEMENT_TIMEOUT = int(os.getenv("GET_WEB_ELEMENT_TIMEOUT") or '3')
