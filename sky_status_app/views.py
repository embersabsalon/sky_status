import requests
import json

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
    print (weather_data)
    context = {'weather_data': weather_data}
    return render(request, 'sky_status_app/index.html', context)
