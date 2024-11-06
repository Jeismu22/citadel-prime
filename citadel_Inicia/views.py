from django.shortcuts import render
from django.utils import timezone
from .models import Post  # Importamos el modelo Post

def post_list(request):
    # Obtener todos los posts publicados, ordenados por fecha de publicación
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    # Pasar los posts a la plantilla como parte del contexto
    return render(request, 'citadel_Inicia/post_list.html', {'posts': posts})
