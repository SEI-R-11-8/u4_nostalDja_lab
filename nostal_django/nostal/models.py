from email.mime import image
from django.db import models

# Create your models here.


class Decade(models.Model):
    start_year = models.CharField(max_length=100)

    def __str__(self):
        return self.start_year


class Fad(models.Model):
    decade = models.ForeignKey(
        Decade, on_delete=models.CASCADE, related_name='fads')
    name = models.CharField(max_length=100)
    image_url = models.TextField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
