from django.http import HttpResponse
from django.shortcuts import render

from weather.forms import GetWeatherForm
from weather.utils import menu, weather_by_city


def get_weather(request):
    if request.method == 'POST':
        form = GetWeatherForm(request.POST)
        if form.is_valid():
            weather = weather_by_city(form.cleaned_data['city'])
        try:
            weather['temp_C'] and weather['FeelsLikeC']
        except (AttributeError, TypeError, KeyError):
            return HttpResponse('Сервис погоды временно недоступен')
        temp = weather['temp_C']
        temp_feel = weather['FeelsLikeC']
        return render(
            request,
            'weather/weather_display.html',
            {'temp': temp, 'temp_feel': temp_feel, 'menu': menu}
        )
    else:
        form = GetWeatherForm()

    form = GetWeatherForm()

    return render(request, 'weather/index.html', {'form': form, 'menu': menu})
