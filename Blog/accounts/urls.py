from django.urls import path
from . import views

urlpatterns = [
        path("register", views.post, name = "blog"),
        path("login", views.home, name = "home"),
        ] 
