from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from import_export.admin import ImportExportModelAdmin

from story.models import Slides, Vehicles, VehicleDetail, Stories, StorieDetail


@admin.register(Slides)
class SlidesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'header', 'sub_header', 'description', 'image', 'created')
    list_per_page = 5

    fieldsets = (
        ('header', {
            'fields': ('id', 'header', 'sub_header', 'description', 'image', 'created')
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '59'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 59})},
    }


@admin.register(Vehicles)
class VehiclesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'header', 'sub_header', 'description', 'image', 'created')
    list_per_page = 5

    fieldsets = (
        ('header', {
            'fields': ('id', 'header', 'sub_header', 'description', 'image', 'created')
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '59'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 59})},
    }


@admin.register(VehicleDetail)
class VehicleDetailAdmin(ImportExportModelAdmin):
    list_display = ('id', 'vehicles', 'header', 'description', 'image', 'created')
    list_per_page = 5

    fieldsets = (
        ('header', {
            'fields': ('id', 'vehicles', 'header', 'description', 'image', 'created')
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '59'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 59})},
    }


@admin.register(Stories)
class StoriesAdmin(ImportExportModelAdmin):
    list_display = (
        'id', 'header',  'description', 'image', 'created')
    list_per_page = 5

    fieldsets = (
        ('header', {
            'fields': (
                'id', 'header',  'description', 'image', 'created')
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '59'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 59})},
    }


@admin.register(StorieDetail)
class StorieDetail(ImportExportModelAdmin):
    list_display = (
        'id', 'stories', 'header', 'image', 'created')
    list_per_page = 5

    fieldsets = (
        ('header', {
            'fields': (
                'id', 'stories', 'header',  'image', 'created')
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '59'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 59})},
    }