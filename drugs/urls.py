from django.contrib.auth import views as views_auth
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info-marihuana/', views.infomarihuana, name='infomarihuana'),
    path('consultas/', views.consultas, name='consultas'),
    path('crear-consulta', views.crearConsulta, name="crearConsulta"),
    path('consultas/eliminar/<int:pk>/', views.consultaEliminar, name='consultaEliminar'),
    path('consulta/responder/', views.consultasResponder, name='consultasResponder'),
    path('consulta/responder/<int:pk>/', views.consultaResponder, name='consultaResponder'),

    path('ingresar/', views_auth.LoginView.as_view(template_name='drugs/login.html'), name='login'),
    path('salir/', views_auth.LogoutView.as_view(next_page='index'), name='logout'),
    path('registrarme/', views.registrar, name='registrar'),
]
