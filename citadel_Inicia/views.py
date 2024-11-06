# citadel_Inicia/views.py
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # Obtener todos los posts
    return render(request, 'ciudadela/post_list.html', {'posts': posts})  # Cambia 'citadel_Inicia' a 'ciudadela'
