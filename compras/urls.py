
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='compras_index'),
]
