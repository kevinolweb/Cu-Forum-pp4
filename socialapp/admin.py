from django.contrib import admin
from .models import *
# from django_summernote.admin import SummernoteModelAdmin

# # Register your models here.
# @admin.register(CreditUnion)
# class CreditUnionAdmin(SummernoteModelAdmin):
#     search_fields = ['name']
#     list_display = ('name',)

# @admin.register(Topic)
# class TopicAdmin(SummernoteModelAdmin):
#     list_display = ('title', 'category', 'creator', 'created_on')
#     search_fields = ['title', 'category']
#     list_filter = ('category', 'created_on')
#     prepopulated_fields = {'slug': ('title',)}
#     summernote_fields = ('summary',)
    
#     def make_trending(self, request, queryset):
#         queryset.update(trending=True)

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('user', 'body', 'topic', 'created',)
#     list_filter = ('topic', 'created')
#     search_fields = ('user', 'body')

# @admin.register(TopicCategory)
# class TopicCategoryAdmin(SummernoteModelAdmin):
#     list_display = ('name',)

