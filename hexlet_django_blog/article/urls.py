from django.urls import path

from hexlet_django_blog.article.views import (
    IndexView,
    ArticleView,
    ArticleFormCreateView,
    ArticleFormEditView,
    ArticleFormDeleteView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='articles_list'),
    # path('<str:tag>/<int:article_id>', views.article_view, name='article'),
    path('create/', ArticleFormCreateView.as_view(), name='article_create'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='article_update'),
    path('<int:id>/delete/', ArticleFormDeleteView.as_view(), name='article_delete'),
    path('<int:id>', ArticleView.as_view(), name='article_view'),
]
