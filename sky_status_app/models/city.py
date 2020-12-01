from django.db import models


class City(models.Model):
    """ Cities loaded from the fixture file which contains their city id
        as listed from the open weather app api

    Fields:
        * city_id           -- ID in open weather app
        * name              -- City name.
        * removed           -- Indicates if this city is deleted or not.
    """
    city_id = models.IntegerField()
    name = models.CharField(max_length=256)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
