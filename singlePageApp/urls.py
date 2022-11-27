
from django.urls import path

from . import views
from posts import views as posts_views


urlpatterns = [
    path("", views.index, name="index"),
    path("sections/<int:num>", views.section, name="section"),
    path("posts/", posts_views.index, name="posts"),
    path("inf/", posts_views.posts, name="inf"),

]






