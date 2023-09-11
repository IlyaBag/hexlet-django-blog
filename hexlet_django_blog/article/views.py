from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse
# from django.shortcuts import redirect
# from django.urls import reverse
from hexlet_django_blog.article.models import Article

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


def article_view(request, tag, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tag}')
