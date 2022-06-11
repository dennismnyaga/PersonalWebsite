from django.db import models
from embed_video.fields import EmbedVideoField

class Pythonister(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    video = EmbedVideoField()
    image = models.ImageField(null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Djangonister(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    video = EmbedVideoField()
    image = models.ImageField(null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    image = models.ImageField(null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


