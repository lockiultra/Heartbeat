from django.db import models

# Create your models here.

class MenuItem(models.Model):
    title = models.CharField(max_length=32, blank=False)
    url = models.URLField(blank=False)