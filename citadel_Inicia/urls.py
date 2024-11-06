# citadel_Inicia/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # La vista para la página principal
]
