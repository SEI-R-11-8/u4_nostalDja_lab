from django.contrib import admin

# Register your models here.
from .models import Decades

admin.site.register(Decades)

from .models import Fads
admin.site.register(Fads)