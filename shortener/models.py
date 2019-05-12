from django.db import models


class Url(models.Model):
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=300, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'url'
