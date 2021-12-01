from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from import_export.admin import ImportExportModelAdmin

from scenic.models import Article, Category, Tag, Avatar

@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    list_display = ('author', 'category', 'title', 'created', 'created')
    list_per_page = 5

    fieldsets = (
        ('xxx', {
            'fields': ('author', 'category', 'tags',  'avatar', 'title', 'body', 'created')
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '59'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 59})},
    }

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('title','created')
    list_per_page = 5

    fieldsets = (
        ('xxx', {
            'fields':  ('title','created')
        }),
    )


admin.site.register(Tag)
admin.site.register(Avatar)