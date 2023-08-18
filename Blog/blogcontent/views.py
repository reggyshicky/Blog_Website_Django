from django.shortcuts import render
from .models import Blog

def postcontent(request):
    posts = Blog.objects.all() #objects.all fetch everything from the db and will store it in posts
    print(posts)
    return render(request, 'postcontent.html', {"posts": posts})

