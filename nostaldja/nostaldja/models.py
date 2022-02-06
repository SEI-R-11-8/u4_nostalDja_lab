from django.db import models


class Decade(models.Model):
  start_year = models.TextField()
  

  def __str__(self):
    return self.start_year

class Fad(models.Model):
  
  name = models.CharField(max_length=100)
  image_url = models.TextField()
  description = models.TextField()
  decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fad' )

  def __str__(self):
    return self.name