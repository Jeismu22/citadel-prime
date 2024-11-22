# citadel_Inicia/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # Obtener todos los posts
    return render(request, 'ciudadela/post_list.html', {'posts': posts})  # Cambia 'citadel_Inicia' a 'ciudadela'

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Buscamos la publicación por su pk
    return render(request, 'blog/post_detail.html', {'post': post})
