from django.urls import path
from . import views

app_name = "enquete"

urlpatterns=[
    path('', views.index_enquete, name='index_enquete'),
    path('resultado/', views.resultados_view, name='resultados_genero')
]