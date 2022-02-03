from django.db import models

# Create your models here.
class decade(models.Model):
    name = models.CharField(max_length=300)
    

    def __str__(self):
        return self.name

class Fad(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    image_url = models.TextField()
    decade = models.ForeignKey(decade, on_delete=models.CASCADE,related_name='fads')

    def __str__(self):
        return self.name