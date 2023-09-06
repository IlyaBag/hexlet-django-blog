from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
class ArticleView(View):

    def get(self, request, *args, **kwargs):
        return redirect(reverse('index', kwargs={'tag': 'python', 'article_id': 42}))
        # return render(request, 'article-index.html', context={'name': 'article'})
# def index(request):
#     return render(request, 'article-index.html', context={'name': 'article'})


def index(request, tag, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tag}')
