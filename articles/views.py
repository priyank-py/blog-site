from django.shortcuts import render, get_object_or_404
from .models import Article

def home(request):
    articles = Article.objects.all().order_by('-published_on')
    if len(articles) > 5:
        articles = articles[:5]
    
    context = {
        'articles': articles,
    }

    return render(request, 'main/index.html', context)

def each_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    body = article.body.split('\n')
    context = {
        'article': article,
        'body': body
    }
    return render(request, 'main/article.html', context)

def contact_us(request):
    return render(request, 'main/contact_us.html')
