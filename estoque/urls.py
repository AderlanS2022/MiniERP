from django.urls import path
from . import views

urlpatterns = [

    path('', views.lista_movimentacoes, name='lista_movimentacoes'),

    path('nova/', views.nova_movimentacao, name='nova_movimentacao'),

]
