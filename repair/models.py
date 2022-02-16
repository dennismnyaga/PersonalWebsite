from django.db import models

class Hardware(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    image = models.ImageField(null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Software(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    image = models.ImageField(null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


