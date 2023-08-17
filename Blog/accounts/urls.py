from django.urls import path
from . import views

urlpatterns = [
        path("login", views.post, name = "login"),
        path("register", views.register, name = "register"),
        ] 
