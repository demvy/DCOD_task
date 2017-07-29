from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Data(models.Model):
    """
    It is model Data with our fields from csv: region, country, value
    """
    region = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    value = models.IntegerField()

    def __unicode__(self):
        return u"%s - %s - %s" % (self.region, self.country, self.value)

    def __str__(self):
        return u"%s - %s - %s" % (self.region, self.country, self.value)
