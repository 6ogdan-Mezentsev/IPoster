from django.contrib import admin

from articles.models import Articles


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title',)
