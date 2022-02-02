from django.urls import path
from . import views

urlpatterns = [
    path('decades', views.decade_get_all, name='decade_get_all'),
    path('<int:fk>/fads', views.fads_by_decade, name='fads_by_decade'),
    path('fad/create', views.fad_create, name='fad_create'),
    path('fad/<int:id>/edit', views.fad_edit, name='fad_edit'),
    path('fad/<int:id>/delete', views.fad_delete, name='fad_delete')
]