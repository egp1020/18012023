from django.urls import path
from AppCoder import views
from AppCoder.views import ContactoListar
urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    #path('profesores', views.profesores, name="Profesores"),
    path('AgregarCanales', views.formularioCargarCanal, name="AgregarCanales"),
    #path('MostrarCanales', views.formularioMostrarCanal, name="MostrarCanales"),
    #path('app_contactos/', ContactoListar.as_view(template_name = "AppCoder/MostrarCanales.html"), name='MostrarCanales'),
    #path('MostrarCanales', views.CursoDetalle.as_view(), name="MostrarCanales"),
    path('curso/list', views.CursoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
    
    path('eliminarCanal/<canal_nombre>/', views.eliminarCanal, name="eliminarCanal"),
    path('MostrarCanales/', views.leerCanal, name="MostrarCanales"),
    path('editarCanal/<canal_nombre>/', views.editarCanal, name="editarCanal"),
    path('buscar/', views.buscar),
    
    ] 

