from django.shortcuts import render, get_object_or_404
from .models import Blog, Project


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'details.html', {'blog': blog})

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})
