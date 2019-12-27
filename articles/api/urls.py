from django.urls import path
from articles.api.views import article_get_data

urlpatterns = [
    path('<int:id>', article_get_data, name="get_data"),
]
