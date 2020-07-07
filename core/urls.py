from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acercade/', views.acercade, name='acercade'),
    path('proceso/', views.proceso, name='proceso'),
    path('venta/', views.venta, name='venta'),
]
