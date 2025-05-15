from django.urls import path
from . import views

urlpatterns=[
    path('', views.index_questao3, name='index_questao3'),
    path('resultado3/', views.resultado_questao3, name='resultado_questao3')
]