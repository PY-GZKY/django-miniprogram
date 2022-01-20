from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from import_export.admin import ImportExportModelAdmin

from story.models import Slides, Vehicles, VehicleDetail


@admin.register(Slides)
class SlidesAdmin(ImportExportModelAdmin):
    list_display = ('header', 'sub_header', 'description', 'image', 'created')
    list_per_page = 5

    fieldsets = (
        ('header', {
            'fields': ('header', 'sub_header', 'description', 'image', 'created')
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '59'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 59})},
    }


@admin.register(Vehicles)
class VehiclesAdmin(ImportExportModelAdmin):
    list_display = ('header', 'sub_header', 'description', 'image', 'created')
    list_per_page = 5

    fieldsets = (
        ('header', {
            'fields': ( 'header', 'sub_header', 'description', 'image', 'created')
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '59'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 59})},
    }


@admin.register(VehicleDetail)
class VehicleDeatilAdmin(ImportExportModelAdmin):
    list_display = ('vehicles', 'header', 'description', 'image', 'created')
    list_per_page = 5

    fieldsets = (
        ('header', {
            'fields': ('vehicles', 'header', 'description', 'image', 'created')
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '59'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 59})},
    }