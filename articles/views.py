from django.shortcuts import render, get_object_or_404
from .models import Article

def home(request):
    articles = Article.objects.all().order_by('-published_on')
    if len(articles) > 5:
        articles = articles[:5]
    
    slugs = [i.slug for i in articles]
    print(slugs)
    
    context = {
        'articles': articles,
        'slugs': slugs,
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


def about(request):
    return render(request, 'main/about.html')

def search_article(request):
    if request.method == 'POST':
        search_text = request.POST.get('searched')
    else:
        search_text = ''
    articles = Article.objects.filter(title__icontains=search_text)
    slugs = [i.slug for i in articles]
    context = {
        'articles': articles,
        'slugs': slugs
    }
    return render(request, 'main/index.html', context)