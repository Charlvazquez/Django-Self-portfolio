from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post(request):
    entradas = Post.objects.all()
    return render(request, 'post.html',{'entradas':entradas})

def detalles(request, post_id):#definir variable para darle un id a entradas de blog
    entrada = get_object_or_404(Post, pk=post_id)
    return render(request,'detalles.html',{"entrada":entrada})