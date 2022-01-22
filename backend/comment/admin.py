# from django.contrib import admin
# from django.db import models
# from django.forms import TextInput, Textarea
# from import_export.admin import ImportExportModelAdmin
#
# from comment.models import Comment
#
# @admin.register(Comment)
# class CommentAdmin(ImportExportModelAdmin):
#     list_display = ('author', 'article', 'parent',  'content', 'created')
#     list_per_page = 5
#
#     fieldsets = (
#         ('xxx', {
#             'fields': ('author', 'article', 'parent',  'content', 'created')
#         }),
#     )
#
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size': '59'})},
#         models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 59})},
#     }
#
