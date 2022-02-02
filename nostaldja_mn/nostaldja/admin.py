from django.contrib import admin

# Register your models here.

from .models import Decade, Fad

admin.site.register(Decade)
admin.site.register(Fad)
