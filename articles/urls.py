from django.urls import path

from articles.views import home, new_articles, user_articles, delete_article, add_to_favorites, remove_from_favorites, favorite_articles, toggle_article_like

app_name = 'articles'

urlpatterns = [
    path('', home, name='home'),
    path('new-articles/', new_articles, name='new_articles'),
    path('my-articles/', user_articles, name='user_articles'),
    path('delete/<int:article_id>/', delete_article, name='delete_article'),
    path('add_to_favorites/<int:article_id>/', add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:article_id>/', remove_from_favorites, name='remove_from_favorites'),
    path('favorite_articles/', favorite_articles, name='favorite_articles'),
    path('like/<int:article_id>/', toggle_article_like, name='toggle_article_like')
]
