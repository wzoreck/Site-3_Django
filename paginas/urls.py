from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Nomeando a url no código como index
    path('sobre/', views.sobre, name='sobre'),
]
