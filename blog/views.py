from django.shortcuts import render
from .models import *

def post_listar(request):
    return render(request, 'blog/post_listar.html', {})
