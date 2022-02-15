from django.db import models

class Tex(models.Model):
    image = models.ImageField(null = True, blank = True)
