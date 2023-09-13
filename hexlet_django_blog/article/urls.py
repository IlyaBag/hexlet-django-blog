from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    # path('<str:tag>/<int:article_id>', views.article_view, name='article'),
    path('<int:article_id>', views.ArticleView.as_view(), name='article_view'),
]
