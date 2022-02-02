from django.urls import path
from . import views

urlpatterns = [
    path('', views.decade_list, name='decade_list'),
    path('fads/', views.fad_list, name='fad_list'),
    path('decades/<int:pk>', views.decade_detail, name='decade_detail'),
    path('fads/<int:pk>', views.fad_detail, name='fad_detail'),
    path('fads/<int:pk>/edit', views.fad_edit, name='fad_edit'),
    path('fads/new', views.fad_create, name='fad_create'),
    path('fads/<int:pk>/delete', views.fad_delete, name='fad_delete'),
]
