from django.shortcuts import render
from django.utils import timezone
from .models import *

def post_listar(request):
    posts = Postear.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
    return render(request, 'blog/post_listar.html', {'posts': posts})
