from django.shortcuts import render, get_object_or_404
from django.views import View
# from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import ArticleForm

# Create your views here.
# def index(request):
#     return render(request, 'article-index.html', context={'name': 'article'})
class IndexView(View):

    def get(self, request, *args, **kwargs):
        # return render(request, 'article-index.html', context={
        #     'name': 'article'
        # })
        # return redirect(reverse('article', kwargs={
            # 'tag': 'python', 'article_id': 42
        # }))
        articles = Article.objects.all()
        return render(request, 'article-index.html', context={
            'articles': articles
        })


# def article_view(request, tag, article_id):
#     return HttpResponse(f'Статья номер {article_id}. Тег {tag}')
class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['article_id'])
        return render(request, 'article-show.html', context={
            'article': article,
        })

class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article-create.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles_list')
        return render(request, 'article-create.html', {'form': form})
