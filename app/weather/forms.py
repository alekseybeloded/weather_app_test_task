from django import forms


class GetWeatherForm(forms.Form):
    city = forms.CharField(max_length=100)
