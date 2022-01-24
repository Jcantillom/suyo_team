from django.db import models
from django.contrib.gis.db import models



class LocationModel(models.Model):
    property = models.CharField(max_length=200, blank=True, null=True)
    name_location = models.CharField(max_length=200)
    latitude = models.CharField(max_length=15)
    longitude = models.CharField(max_length=15)
    user = models.ManyToManyField('users.User')

    class Meta:
        db_table = "suyo_locations"



