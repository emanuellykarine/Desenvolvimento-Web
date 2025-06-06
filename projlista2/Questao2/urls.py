from django.urls import path

from . import views

app_name = "Questao2"
urlpatterns=[
    path('', views.index2, name='index2'),
    path('previsao/', views.previsao_view, name='previsao')
]