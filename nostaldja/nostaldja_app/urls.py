from django.urls import path
from . import views

urlpatterns = [
    path('decades', views.decade_get_all, name='decade_get_all'),
    path('<int:fk>/fads', views.fad_by_decade, name='fad_by_decade')
]