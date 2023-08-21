from django.shortcuts import render
from .models import Blog

def postcontent(request):
    posts = Blog.objects.all() #objects.all fetch everything from the db and will store it in posts
    context = {
        "posts": posts
    }
    return render(request, 'postcontent.html', context)

def detail_page(request, pk):  # PK is the primary key
    post = Blog.objects.get(pk=pk) #get() returns only one
    context = {
        "post": post
    }
    
    return render(request, "details_page.html", context)