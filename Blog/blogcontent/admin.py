from django.contrib import admin
from .models import Category
# Register your models here.
from .models import Blog
admin.site.register(Blog)
admin.site.register(Category)
