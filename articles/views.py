from django.shortcuts import get_object_or_404, render, redirect

from articles.models import Articles, Favorite
from .forms import CreateArticleForm
from notification.models import Notification


def home(request):
    context = {'articles': Articles.objects.all()}

    if request.user.is_authenticated:
        favorite_articles_ids = Favorite.objects.filter(user=request.user).values_list('article_id', flat=True)
        liked_articles = request.user.liked_articles.values_list('id', flat=True)
        context.update({
            'favorite_articles': favorite_articles_ids,
            'liked_articles': liked_articles,
        })

    return render(request, 'articles/home.html', context)


def user_articles(request):
    context = {
        'articles': Articles.objects.filter(author=request.user),
    }

    return render(request, 'articles/user_articles.html', context)


def new_articles(request):
    if request.method == 'POST':
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            form.save()
            """Сохранение формы: form.save() сохраняет данные формы в базу данных. 
            Это возможно благодаря тому, что форма является моделевой формой (ModelForm), 
            которая знает, как преобразовать данные формы в экземпляр модели"""
            return redirect('articles:home')
    else:
        form = CreateArticleForm()

    return render(request, 'articles/new_articles.html', {'form': form})


def delete_article(request, article_id):
    article = Articles.objects.get(id=article_id, author=request.user)
    article.delete()

    return redirect('articles:user_articles')


def add_to_favorites(request, article_id):
    article = Articles.objects.get(id=article_id)
    Favorite.objects.create(user=request.user, article=article)

    previous_page = request.META.get('HTTP_REFERER', '/')
    return redirect(previous_page)


def remove_from_favorites(request, article_id):
    article = Articles.objects.get(id=article_id)
    Favorite.objects.filter(user=request.user, article=article).delete()

    previous_page = request.META.get('HTTP_REFERER', '/')
    return redirect(previous_page)


def favorite_articles(request):

    favorite_articles_ids = Favorite.objects.filter(user=request.user).values_list('article_id', flat=True)
    articles = Articles.objects.filter(id__in=favorite_articles_ids)

    context = {
        'articles': articles,
    }

    return render(request, 'articles/favorite_articles.html', context)


def toggle_article_like(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    if request.user in article.likes.all():
        article.likes.remove(request.user)
    else:
        article.likes.add(request.user)

        if article.author != request.user:
            Notification.objects.create(
                recipient=article.author,
                sender=request.user,
                message=f"{request.user.username} лайкнул вашу статью «{article.title}»",
            )

    previous_page = request.META.get('HTTP_REFERER', '/')
    return redirect(previous_page)

