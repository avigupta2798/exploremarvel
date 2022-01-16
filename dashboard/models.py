from django.db import models

# Create your models here.

class Comic(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True)
    format = models.CharField(max_length=1000, null=True)
    issueNumber = models.IntegerField()
    comic_thumbnail_path = models.CharField(max_length=400)

class Characters(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True)
    char_thumbnail_path = models.CharField(max_length=400)
    comic = models.ManyToManyField(Comic)

class Events(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True)
    char_thumbnail_path = models.CharField(max_length=400)
    comic = models.ManyToManyField(Comic)
    character = models.ManyToManyField(Characters)

class Series(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True)
    char_thumbnail_path = models.CharField(max_length=400)
    comic = models.ManyToManyField(Comic)
    character = models.ManyToManyField(Characters)
    event = models.ManyToManyField(Events)