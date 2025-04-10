from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import inicio, agregar_prenda, buscar_prenda, acerca_de_mi, registro, lista_productos

urlpatterns = [
    path("", inicio, name="inicio"),
    path("agregar/", agregar_prenda, name="agregar_prenda"),
    path("buscar/", buscar_prenda, name="buscar_prenda"),
    path("about/", acerca_de_mi, name="acerca_de_mi"),
    path("login/", LoginView.as_view(template_name="ropa/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path('registro/', registro, name='registro'),
    path("productos/", lista_productos, name="lista_productos"),
]
