from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<slug>', views.each_article, name="each_article"),
    path('contact/', views.contact_us, name="contact")
]
