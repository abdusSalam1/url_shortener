from django.conf.urls import url

from shortener import views

urlpatterns = [
    url(r'^$', views.ShortenerView.get_url_shortener_view, name='index')
]
