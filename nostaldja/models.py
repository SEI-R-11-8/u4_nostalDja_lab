from django.db import models

# Create your models here.
class Decades(models.Model):
    start_year = models.CharField(max_length=4)

    def __str__(self):
        return self.start_year

class Fads(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.TextField()
    description = models.CharField(max_length=100)
    decade = models.ForeignKey(Decades, on_delete=models.CASCADE, related_name='fad')

    def __str__(self):
        return self.name