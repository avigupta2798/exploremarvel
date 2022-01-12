from django.db import models

# Create your models here.

class Comic(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    issueNumber = models.IntegerField()
    comic_thumbnail_path = models.CharField(max_length=400)
    comic_thumbnail_extension = models.CharField(max_length=5)

class Characters(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    char_thumbnail_path = models.CharField(max_length=400)
    char_thumbnail_extension = models.CharField(max_length=5)
    comic = models.ManyToManyField(Comic)

class Events(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    char_thumbnail_path = models.CharField(max_length=400)
    char_thumbnail_extension = models.CharField(max_length=5)
    comic = models.ManyToManyField(Comic)

class Series(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    char_thumbnail_path = models.CharField(max_length=400)
    char_thumbnail_extension = models.CharField(max_length=5)
    comic = models.ManyToManyField(Comic)