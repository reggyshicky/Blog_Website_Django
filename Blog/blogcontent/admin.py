from django.contrib import admin
from .models import Category, Comment, Review
# Register your models here.
from .models import Blog
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Review)