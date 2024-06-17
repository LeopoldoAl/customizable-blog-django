from django.urls import path
from my_blog.views import show_articles, send_articles_body

urlpatterns = [
    path("", show_articles, name='index'),
    path("<slug:slug>", send_articles_body, name ='post'),
]
