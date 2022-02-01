from django.db import models

# Create your models here.


class Decade(models.Model):
    start_year = models.CharField(max_length=200)

    def __str__(self):
        return self.start_year


class Fad(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.TextField(max_length=500)
    description = models.TextField(max_length=600)
    decade = models.ForeignKey(
        Decade, on_delete=models.CASCADE, related_name='fads')

    def __str__(self):
        return self.name
