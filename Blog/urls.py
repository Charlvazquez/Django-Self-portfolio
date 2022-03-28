from django.urls import path
from .views import post, detalles

app_name ='blog' #funcion url para cada blog

urlpatterns = [
    path('', post ,name='post'), #ruta de post
    path('<int:post_id>', detalles, name="detalles"), #ruta para mostrar cada entrada de blog
]