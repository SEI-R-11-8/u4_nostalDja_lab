from django.urls import path
from . import views

urlpatterns = [
    path('', views.decade_list, name='decade_list'),
    path('fad_list/', views.fad_list, name='fad_list'),
    path('decades/<int:pk>', views.decade_detail, name='decade_detail'),
    path('fads/<int:pk>', views.fad_detail, name='fad_detail'),
    path('decade/new', views.decade_create, name='decade_create'),
    path('fad/new', views.fad_create, name='fad_create'),
    path('decades/<int:pk>/delete', views.decade_delete, name='decade_delete'),
    path('fads/<int:pk>/delete', views.fad_delete, name='fad_delete'),

]