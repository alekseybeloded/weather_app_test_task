from django.urls import path

from weather import views

urlpatterns = [
    path('', views.get_weather, name='get_weather'),
    path('choose-city/', views.choose_city, name='choose_city'),
]
