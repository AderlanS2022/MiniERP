
from django.urls import path
from . import views

app_name = "pdv"

urlpatterns = [
    path("", views.pdv_home, name="home"),                 # /pdv/
    path("abrir-caixa/", views.abrir_caixa, name="abrir_caixa"),  # /pdv/abrir-caixa/
    path("caixa/", views.caixa_fullscreen, name="caixa"),  # /pdv/caixa/
    path("fechar-caixa/", views.fechar_caixa, name="fechar_caixa"),  # /pdv/fechar-caixa/
]