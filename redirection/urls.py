from django.conf.urls import url

from redirection import views

urlpatterns = [
    url(r'^$', views.redirect_to_site)
]
