from django.shortcuts import render
from .models import Article, Category

def liste_articles(request):
    category = request.GET.get('categorie')
    if category:
        articles = Article.objects.filter(categorie=category)
    else:
        articles = Article.objects.all()
    categories = Category.objects.all()
    for article in articles:
        if article.promotion:
            article.promo_price = article.prix - (article.prix * article.promotion.pourcentage / 100)
        else:
            article.promo_price = None
    return render(request, 'articles/liste_articles.html', {'articles': articles, 'categories': categories})  # Modification de cette ligne


def home(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'home.html', context)
