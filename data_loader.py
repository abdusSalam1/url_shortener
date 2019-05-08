import logging
import os
import re

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'url_shortener.settings')
django.setup()

from shortener.models import Url


def load_initial_data():
    try:
        words = open(os.path.abspath("data/words.txt"), 'r').readlines()
        urls = []
        for word in words:
            if not word == "\n":
                urls.append(Url(name=get_word(word), url=None, timestamp=None))
        Url.objects.bulk_create(urls)
    except Exception as ex:
        logging.error("Error running script for loading initial data " + ex)


def get_word(word):
    proper_word = re.sub('[^A-Za-z0-9]+', '', word)
    return proper_word.lower()


if __name__ == '__main__':
    print("Populating initial data started")
    load_initial_data()
    print("Populating initial data completed")
