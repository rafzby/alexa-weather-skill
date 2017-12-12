from dotenv import load_dotenv
from os.path import join, dirname
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path, verbose=True)

OPEN_WEATHER_MAP = {
    'BASE_URL': 'http://api.openweathermap.org/data/2.5/weather',
    'API_KEY': os.environ.get('API_KEY'),
    'CITY': os.environ.get('CITY'),
}
