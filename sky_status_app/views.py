from django.shortcuts import render


def index(request):
    return render(request, 'sky_status_app/weather.html')
