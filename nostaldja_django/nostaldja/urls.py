
from django.urls import path
from . import views

urlpatterns = [
    # create decade
    path('decades/new', views.decade_create, name="decade_create"),
    # read decade
    path('', views.decade_list, name='decade_list'),
    # update decade
    path('decades/<int:pk>/edit', views.decade_edit,  name="decade_edit"),
    # delete decade
    path('decades/<int:pk>/delete', views.decade_delete, name="decade_delete"),
    # decade detail
    path('decades/<int:pk>', views.decade_detail, name='decade_detail'),
    # create fad
    path('fads/new', views.fad_create, name='fad_create'),
    # read fad
    path('fads/', views.fad_list, name='fad_list'),
    # update fad
    path('fads/<int:pk>/edit', views.fad_edit, name='fad_edit'),
    # delete fad
    path('fads/<int:pk>/delete', views.fad_delete, name='fad_delete'),
    # fad detail
    path('fads/<int:pk>', views.fad_detail, name='fad_detail'),

]
