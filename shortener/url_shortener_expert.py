import re
from datetime import datetime

from shortener.models import Url


class UrlShortenerExpert:
    BASE_USER = "http://localhost:8000"

    def shorten(long_url):
        splitted_url = re.split('[/ -]', long_url)
        results = Url.objects.filter(name__in=splitted_url, url=None)
        if not results.first() is None:
            url_from_db = results.first()
            UrlShortenerExpert.update_url(url_from_db, long_url)
            return UrlShortenerExpert.BASE_USER + "/" + url_from_db.name
        else:
            if UrlShortenerExpert.has_used_key():
                used_url = UrlShortenerExpert.get_old_used_key()
                UrlShortenerExpert.update_url(used_url, long_url)
                return UrlShortenerExpert.BASE_USER + "/" + used_url.name
            else:
                new_url = Url.objects.all().first()
                UrlShortenerExpert.update_url(new_url, long_url)
                return UrlShortenerExpert.BASE_USER + "/" + new_url.name

    @staticmethod
    def has_used_key():
        url_without_date = Url.objects.filter(url=None).count()
        return url_without_date == 0

    @staticmethod
    def get_old_used_key():
        results = Url.objects.all().order_by('-timestamp')
        return results.first()

    def update_url(url_from_db, original_url):
        if not url_from_db is None:
            url_from_db.url = original_url
            url_from_db.timestamp = datetime.now()
            url_from_db.save()
