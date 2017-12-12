from settings import OPEN_WEATHER_MAP
import requests
import json


def get_weather_data():
    url = OPEN_WEATHER_MAP['BASE_URL'] + '?q={}&appid={}'.format(OPEN_WEATHER_MAP['CITY'],
                                                                 OPEN_WEATHER_MAP['API_KEY'])

    session = requests.Session()
    session.headers.update({'User-Agent': 'Alexa Weather Skill'})
    response = session.get(url)

    data = json.loads(response.content.decode('utf-8'))

    return data
