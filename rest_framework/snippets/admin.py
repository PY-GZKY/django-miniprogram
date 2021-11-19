from django.contrib import admin

# Register your models here.
from django.forms import TextInput, Textarea
from django.db import models

from import_export.admin import ImportExportModelAdmin
from .models import Snippet


# 文章
@admin.register(Snippet)
class SnippetAdmin(ImportExportModelAdmin):
    list_display = ('title', 'code', 'language', 'style', 'owner', 'created')
    # search_fields = ('title', 'desc', 'content')
    # list_filter = ('category', 'tag', 'add_time')
    # list_editable = ('category', 'open_comment', 'is_recommend', 'is_open')
    # readonly_fields = ('cover_admin',)
    list_per_page = 5

    fieldsets = (
        ('文章', {
            'fields': ('title', 'code', 'language', 'style', 'owner')
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '59'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 59})},
    }

"""
created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(
        choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()
"""
