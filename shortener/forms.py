from django import forms


class UrlShortenerForm(forms.Form):
    url = forms.CharField()
