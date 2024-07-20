from django.urls import path

from weather import views

urlpatterns = [
    path('', views.get_weather, name='home'),
]
