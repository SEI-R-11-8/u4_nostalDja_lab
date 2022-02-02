from django.db import models

# Create your models here.


class Decade(models.Model):
    start_year = models.CharField(max_length=200)

    def __str__(self):
        return self.start_year


class Fad(models.Model):
    decade = models.ForeignKey(
        Decade, on_delete=models.CASCADE, related_name='decades')
    name = models.CharField(max_length=500, default="no name")
    image_url = models.CharField(max_length=500, default="no image URL")
    description = models.CharField(max_length=500, default='no description')

    def __str__(self):
        return self.name
