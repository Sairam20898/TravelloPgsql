from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    disc = models.CharField(max_length=1000)
    price = models.IntegerField(default=None)
    offer = models.BooleanField(default=False)
