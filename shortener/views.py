from django.shortcuts import render

from shortener.url_shortener_expert import UrlShortenerExpert
from . import forms


def get_url_shortener_view(request):
    short_url = ""
    form = forms.UrlShortenerForm()
    if request.method == 'GET':
        form = forms.UrlShortenerForm(request.GET)
        if form.is_valid():
            long_url = form.cleaned_data['url']
            short_url = UrlShortenerExpert.shorten(long_url)
    return render(request, 'shortener/index.html', {'form': form, 'short_url': short_url})
