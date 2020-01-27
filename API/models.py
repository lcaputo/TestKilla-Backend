from django.db import models
from django import forms

class genres(models.Model):
    genederID = models.IntegerField()
    name = models.CharField(max_length=50)

class movies(models.Model):
    title = models.CharField(max_length=200)
    production_company = models.CharField(max_length=200)
    vote_average = models.FloatField()
    genres = models.ForeignKey(to=genres, on_delete=models.CASCADE)
    overview = models.CharField(max_length=200)
    release_date = models.DateTimeField()
    original_language = models.CharField(max_length=200)
    popularity = models.FloatField()
    cover_image = models.CharField(max_length=200)
    backdrop_image = models.CharField(max_length=200)
    video = models.CharField(max_length=200)
    adult = models.BooleanField()