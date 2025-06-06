from django.urls import path

from . import views

app_name = "Questao1"
urlpatterns=[
    path('', views.index, name='index'),
    path('comentarios/', views.lista_comentarios_view, name='comentarios')
]