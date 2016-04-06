from __future__ import unicode_literals

from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __unicode__(self):
        return self.name

class Event(models.Model):
    location = models.ForeignKey('meetup.Location')
    date = models.DateField()

    def __unicode__(self):
        return unicode(self.date)
