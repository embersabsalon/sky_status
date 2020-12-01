import requests
import json
import os

from django.shortcuts import render
from django.conf import settings


def index(request):
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?id=1717512&appid={settings.OPEN_WEATHER_API_KEY}'
    r = requests.get(weather_url)
    loaded_data = json.loads(r.text)
    weather_data = {
        'name': loaded_data['name'],
        'weather': loaded_data['weather'][0]['main'],
        'icon': loaded_data['weather'][0]['icon'],
        'wind': loaded_data['wind']['speed'],
        'temp': loaded_data['main']['temp']
    }
    context = {'weather_data': weather_data}

    fixture_file = os.path.abspath(os.path.join(
        os.path.dirname(__file__), './fixtures/city_list.json'))
    with open(fixture_file) as f:
        cities_list = json.loads(f.read())
    print (cities_list)
    return render(request, 'sky_status_app/index.html', context)
