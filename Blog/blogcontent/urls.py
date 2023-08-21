from django.urls import path
from . import views

urlpatterns = [
        path('', views.postcontent, name = 'content'),
        path("details/<int:pk>", views.detail_page, name="details"),
        ]

