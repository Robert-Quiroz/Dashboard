from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = '_index'), #'ruta dle nevegador',views.funcion que quiero ejecutar,'comentario para mi yo futuro'
    path('get', views.getLoadsDoftBD, name = 'get_loads'),
    path('post', views.newsLoadsDoftDB, name = 'post_loads'),
    path('prueba', views.prueba, name = 'prueba_loads'),
    path('probando', views.GetLastReadyData, name = 'consumir la api')     
]
