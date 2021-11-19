from django.contrib import admin

# Register your models here.
from django.forms import TextInput, Textarea
from django.db import models

from import_export.admin import ImportExportModelAdmin
from .models import Snippet, Entitie


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


@admin.register(Entitie)
class EntitieAdmin(ImportExportModelAdmin):
    list_display = ('id', 'header', 'original_header', 'description', 'original_description', 'video', 'image', 'duration_raw', 'duration')
    list_per_page = 5

    fieldsets = (
        ('xxx', {
            'fields': ('id', 'header', 'original_header', 'description', 'original_description', 'video', 'image', 'duration_raw', 'duration')
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '59'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 59})},
    }