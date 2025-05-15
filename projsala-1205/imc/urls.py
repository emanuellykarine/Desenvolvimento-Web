from django.urls import path
from . import views

app_name = "imc"
urlpatterns=[ 
    path('', views.index,name='index'),
    # path("calcular/", views.calcular, name='calcular'), #Caminho do calcula soma
    # path ('calcular/<int:altura>/<int:peso>/', views.calcular_imc, name='calcular_imc'),
    path('calcular/', views.calcular_imc_view, name='calcular_imc') #Caminho utilizando o template
    #View que trata a requisição calcular
]