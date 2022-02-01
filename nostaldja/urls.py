from django.urls import path
from . import views

urlpatterns = [
    # VIEW LISTS
    path('', views.decade_list, name='decade_list'),
    path('fads/', views.fad_list, name='fad_list'),

    # VIEW DETAILS
    path('decades/<int:pk>', views.decade_detail, name='decade_detail'),
    path('fads/<int:pk>', views.fad_detail, name='fad_detail'),

    # CREATE
    path('decades/new', views.decade_create, name='decade_create'),
    path('fads/new', views.fad_create, name='fad_create'),

    # EDIT
    path('decades/<int:pk>/edit', views.decade_edit, name='decade_edit'),
    path('fads/<int:pk>/edit', views.fad_edit, name='fad_edit'),

    # DELETE
    path('decades/<int:pk>/delete', views.decade_delete, name='decade_delete'),
    path('fads/<int:pk>/delete', views.fad_delete, name='fad_delete')
]
