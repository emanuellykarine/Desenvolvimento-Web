from django.urls import path
from . import views

urlpatterns=[
    path('', views.index_questao2, name='index_questao2'),
    path('resultado2/', views.resultado_questao2, name='resultado_questao2')
]