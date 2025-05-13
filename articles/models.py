from django.db import models
from django.conf import settings


class Articles(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_articles', blank=True)

    class Meta:
        ordering = ['-date']  # сортировка по дате создания


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'article')  # один и тот же пользователь не может добавить одну
                                               # и ту же статью в избранное несколько раз
