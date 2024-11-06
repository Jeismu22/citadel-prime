from django.shortcuts import render

def post_list(request):
    return render(request, 'citadel_Inicia/post_list.html', {})

# Create your views here.
