from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'Home'), #'ruta del nevegador',views.funcion,'comentario para mi yo futuro'
    path('index.html', views.index, name = 'index.html'),
    path('charts.html', views.charts, name = 'charts.html'),
    path('tables.html', views.tables, name = 'tables.html'),
    path('login.html', views.login, name = 'login.html'),
    path('register.html', views.register, name = 'register.html'),
    path('forgot-password.html', views.forgotPassword, name = 'forgot-password.html'),
    path('get', views.getLoadsDoftBD, name = 'get_loads'), #ok
    path('post', views.newsLoadsDoftDB, name = 'post_loads'),#ok
    path('prueba', views.prueba, name = 'prueba_loads'),#ok
    #path('createProject', views.createProject, name = 'createProject'),
    path('getAProject', views.getAProject, name = 'getAProject'),#ok
    path('runProject', views.runProject, name = 'runProject'), #ok
    path('ListAllProjects', views.ListAllProjects, name = 'ListAllProjects'),#ok
    path('getARun', views.getARun, name = 'getARun'), #ok
    path('getDataForRun', views.getDataForRun, name = 'getDataForRun'),#ok
    path('cancelRun', views.cancelRun, name = 'cancelRun'), #ok
    path('deleteRun', views.deleteRun, name = 'deleteRun'),#ok
    path('GetLastReadyData', views.GetLastReadyData, name = 'GetLastReadyData'),#ok
    path('newsUsers', views.newsUsers, name = 'crear nuevo usurio'),
    path('getOneUser', views.getOneUser, name = 'consultar usuario por cedula'),
    path('getUsersByNames', views.getUsersByNames, name = 'consultar usurio por nombres'),
    path('updateUsers', views.updateUsers, name = 'actualizar un usuario'),
    path('deleteUsers', views.deleteUsers, name = 'eliminar un usuario')     
]
