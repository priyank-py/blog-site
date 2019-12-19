from django.shortcuts import render
from .models import Article

def home(request):
    articles = Article.objects.all().order_by('-published_on')
    if len(articles) > 5:
        articles = articles[:5]
    
    context = {
        'articles': articles,
    }

    return render(request, 'main/index.html', context)
