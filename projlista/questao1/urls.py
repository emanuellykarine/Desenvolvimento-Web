from django.urls import path
from . import views

urlpatterns=[
    path('', views.index_questao1, name='index_questao1'),
    path('resultado1/', views.resultado_questao1, name='resultado_questao1')
]