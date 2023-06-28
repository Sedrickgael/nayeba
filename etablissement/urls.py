from django.urls import path
from . import views

urlpatterns = [
    path('unid', views.unid, name='unid'),
    path('esn', views.esn, name='esn'),
    path('formations', views.formation, name='formations'),
    path('licence', views.licence, name='licence'),
    path('bts', views.bts, name='bts'),
    path('master', views.master, name='master'),
]