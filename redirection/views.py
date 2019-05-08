from django.shortcuts import redirect
from django.views import View

from shortener.models import Url


class RedirectionView(View):

    def redirect_to_site(request):
        key = request.path.strip("/")
        if not key == "favicon.ico":
            url = Url.objects.filter(name=key).first()
            return redirect(url.url)
