from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.

class Project(models.Model):
    titulo = CharField(max_length=150)
    descripcion = CharField(max_length=100)
    imagen = ImageField(upload_to='portafolio/images/')
    url= URLField(blank=True)
