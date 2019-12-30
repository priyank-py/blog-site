from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from articles.models import Article
from articles.api.serializer import ArticleSerializer

@api_view(['GET',])
def article_get_data(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

@api_view(['PUT',])
def article_update_data_view(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Data updated!"
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
def article_add_data_view(request):
    
    article = Article()
    if request.method == "POST":
        serializer = ArticleSerializer(article, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Data Added!"
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
