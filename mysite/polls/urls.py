# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen'
__email__ = 'jaer@nmbu.no'


from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index')
]
