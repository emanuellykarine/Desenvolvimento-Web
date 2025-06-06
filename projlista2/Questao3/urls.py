from django.urls import path

from . import views

app_name = "Questao3"
urlpatterns=[
    path('', views.index3, name='index3'),
    path('frete/', views.frete_view, name='frete')
]