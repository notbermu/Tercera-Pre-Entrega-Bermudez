from django.db import models

# Create your models here.


class Players(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    sport = models.CharField(max_length=15)
    country = models.CharField(max_length=30)
    team = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}" 


class Songs(models.Model):
    name = models.CharField(max_length=20)
    artist = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.artist}"


class Movies(models.Model):
    name = models.CharField(max_length=30)
    protagonist = models.CharField(max_length=20)
    year = models.IntegerField()
    streaming = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.streaming}"

