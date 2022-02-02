from django.db import models

class Decade(models.Model):
    start_year = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.start_year

class Fad(models.Model):
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')
    name = models.CharField(max_length=100)
    image_url = models.TextField(null=True)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name