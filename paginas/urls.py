from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Este name utilizamos para poder referênciar mais facilmente a url no código,
    # Utilizaremos o nome dado a url para "linkar" as paáginas através do href=""
    path('sobre/', views.sobre, name='sobre'),
]
