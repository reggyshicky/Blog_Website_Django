from django.urls import path
from . import views

urlpatterns = [
        path('', views.postcontent, name = 'content'),
        path("details/<int:pk>", views.detail_page, name="details"),
        path("categories", views.all_categories, name="categories"),
        path("category/<str:the_category>", views.each_category, name="each_category"),
        path("comment/<int:pk>", views.comment, name="comment"),
        path("review/<int:pk>", views.review, name="review")
        ]
