from django.contrib import admin
from .models import Category, Comment
# Register your models here.
from .models import Blog
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)
