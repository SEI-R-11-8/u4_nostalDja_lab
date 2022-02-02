from django.db import models

# Create your models here.

class Decade(models.Model):
  # name=models.CharField(max_lenght=100)
  start_year=models.CharField(max_length=4)
  def __str__(self):
    return self.start_year

class Fad(models.Model):
  decade= models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')
  name=models.CharField(max_length=100)
  image_url= models.CharField(max_length=200, null=True)
  description= models.CharField(max_length=400, null=True)

  def __str__(self):
          return self.name