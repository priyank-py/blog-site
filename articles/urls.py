from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('article/<int:id>', views.each_article, name="each_article")
]
