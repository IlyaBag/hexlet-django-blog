from django.shortcuts import render
from django.views import View

# Create your views here.
class ArticleView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'article-index.html', context={'name': 'article'})
# def index(request):
#     return render(request, 'article-index.html', context={'name': 'article'})
