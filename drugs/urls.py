from django.contrib.auth import views as views_auth
from django.urls import path, include, re_path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
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
    path('reset/password_reset', PasswordResetView.as_view(template_name='drugs/password_reset_forms.html', email_template_name="registration/password_reset_email.html"), name = 'password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='drugs/password_reset_done.html'), name = 'password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='drugs/password_reset_confirms.html'), name = 'password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='drugs/password_reset_complete.html') , name = 'password_reset_complete'),
]
