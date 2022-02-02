from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_base, name='base'),
    path('decades/', views.decade_all, name='decade_list'),
    path('fads/', views.fad_all, name='fad_list'),
    path('decade/<int:pk>', views.decade_detail, name='decade_detail'),
    path('fad/<int:pk>', views.fad_detail, name='fad_detail'),
    path('decades/new', views.decade_create, name='decade_create'),
    path('fads/new', views.fad_create, name='fad_create'),
    path('decades/<int:pk>/edit', views.decade_edit, name='decade_edit'),
    path('fads/<int:pk>/edit', views.decade_edit, name='fad_edit'),
    path('decades/<int:pk>/delete', views.decade_delete, name='decade_delete'),
    path('fads/<int:pk>/delete', views.decade_delete, name='fad_delete')
]
