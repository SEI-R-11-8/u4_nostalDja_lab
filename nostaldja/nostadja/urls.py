from django.urls import path
from . import views


urlpatterns = [
    path('', views.decade_list, name='decade_list'),
    path('fads/', views.fads_list, name='fads_list'),
    path('decades/<int:pk>', views.decade_detail, name='decade_detail'),
    path('fads/<int:pk>', views.fads_detail, name='fads_detail'),
    path('decades/new', views.decade_create, name='decade_create'),
    path('fads/new', views.fads_create, name='fads_create'),
    path('decades/<int:pk>/edit', views.decade_edit, name='decade_edit'),
    path('fads/<int:pk>/edit', views.fads_edit, name='fads_edit'),
    path('decades/<int:pk>/delete', views.decade_delete, name='decade_delete'),
    path('fads/<int:pk>/delete', views.fads_delete, name='fads_delete')
]
