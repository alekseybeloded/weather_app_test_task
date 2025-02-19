from django.shortcuts import redirect, render

from weather.forms import GetWeatherForm
from weather.utils import menu, weather_by_city


def get_weather(request):
    if request.method == 'POST':
        form = GetWeatherForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather = weather_by_city(city)
            try:
                temp = weather['temp_C']
                temp_feel = weather['FeelsLikeC']
                request.session['weather'] = {
                    'city': form.cleaned_data['city'],
                    'temp': temp,
                    'temp_feel': temp_feel,
                }
                return render(
                request,
                'weather/weather_display.html',
                {'temp': temp, 'temp_feel': temp_feel, 'city': city, 'menu': menu}
            )
            except (AttributeError, TypeError, KeyError):
                return render(request, 'weather/error.html', {'form': form})
    else:
        form = GetWeatherForm()

    if 'weather' in request.session:
        weather = request.session['weather']
        return render(
            request,
            'weather/weather_display.html',
            {
                'temp': weather['temp'],
                'temp_feel': weather['temp_feel'],
                'city': weather['city'],
                'menu': menu,
            }
        )

    return render(request, 'weather/index.html', {'form': form})


def choose_city(request):
    if 'weather' in request.session:
        del request.session['weather']
    return redirect('get_weather')


def page_not_found(request, exception):
    return render(request, 'weather/page_not_found.html')
