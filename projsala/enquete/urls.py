from django.urls import path
from . import views

urlpatterns=[
    path('', views.index_enquete, name='index_enquete'),
    path('resultado/', views.resultados, name='resultados_genero')
]