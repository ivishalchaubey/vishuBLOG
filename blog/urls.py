from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index),
    path("blog/<id>", views.blog_post_view),
    path("about_me/",views.about_me)
]
