from django.urls import path
from .views import home_produtos

app_name = 'Produtos'

urlpatterns = [

        path('', home_produtos , name ='home')
]


#refencia pq nao tem como saber se voce quer listar , ai o appname especifica isso