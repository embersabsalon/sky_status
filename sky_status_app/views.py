import requests
import json
import os

from django.shortcuts import render
from django.conf import settings

from sky_status_app.models.city import City


def index(request):
    city_name = request.GET.get('city', '')
    city = City.objects.filter(name__contains=city_name).first()
    context = {}
    if city:
        weather_url = f'http://api.openweathermap.org/data/2.5/weather?id={city.city_id}&appid={settings.OPEN_WEATHER_API_KEY}'
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
    elif city_name and not city:
        context = {'message': 'City not found.'}
    return render(request, 'sky_status_app/index.html', context)
