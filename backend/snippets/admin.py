from django.contrib import admin
from django.db import models
# Register your models here.
from django.forms import TextInput, Textarea
from import_export.admin import ImportExportModelAdmin

from .models import Snippet, Entitie, Site, BookInfo


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


@admin.register(BookInfo)
class BookInfoAdmin(ImportExportModelAdmin):
    list_display = ('btitle', 'bpub_date', 'bread',  'bcomment', 'isDelete', 'logo')
    list_per_page = 5

    fieldsets = (
        ('xxx', {
            'fields': ('btitle', 'bpub_date', 'bread',  'bcomment', 'isDelete', 'logo')
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '59'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 59})},
    }


@admin.register(Entitie)
class EntitieAdmin(ImportExportModelAdmin):
    list_display = (
        'id', 'header', 'original_header', 'description', 'original_description', 'video', 'image', 'duration_raw',
        'duration')
    list_per_page = 5

    fieldsets = (
        ('xxx', {
            'fields': (
                'id', 'header', 'original_header', 'description', 'original_description', 'video', 'image',
                'duration_raw',
                'duration')
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '59'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 59})},
    }


# 站点设置
@admin.register(Site)
class SiteAdmin(ImportExportModelAdmin):
    list_display = ('site_name', 'site_year', 'site_title', 'type_chinese', 'type_english', 'home_title',
                    'my_mail', 'site_keywords', 'site_desc', 'domain_url', 'site_avatar', 'about_name', 'about_desc')
    readonly_fields = ('avatar_data',)
    fieldsets = (
        ('站点设置', {
            'fields': (
                'site_name', 'site_year', 'site_title', 'type_chinese', 'type_english', 'home_title', 'my_mail')
        }),
        ('Html meta信息', {
            'fields': ('site_keywords', 'site_desc'),
        }
         ),
        ('about信息', {
            'fields': ('site_avatar', 'avatar_data', 'about_name', 'about_desc'),
        }),
    )
