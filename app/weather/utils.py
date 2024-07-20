import os

import requests
from django.http import JsonResponse
from dotenv import load_dotenv

load_dotenv()

menu = [
    {'title': 'Choose another city', 'url_name': 'choose_city'},
]


def weather_by_city(city_name):
    api_url = os.getenv('API_URL', default='http://api.worldweatheronline.com/premium/v1/weather.ashx')
    params = {
        'key': os.getenv('API_KEY', default='a9e8d05689e64f64bbe142520241807'),
        'q': city_name,
        'format': 'json',
        'num_of_days': 1,
        'lang': 'ru',
    }
    try:
        result = requests.get(api_url, params=params)
        result.raise_for_status()
        weather = result.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except (IndexError, TypeError):
                    return False
    except (requests.RequestException):
        return False
    return JsonResponse(weather)
