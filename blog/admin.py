from django.contrib import admin #in hast
from .models import *
class CommentInline(admin.StackedInline): # new
    model = Comment
#class CommentInline(admin.TabularInline): # new
#    model = Comment

class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
    CommentInline,
    ]
admin.site.register(blog, ArticleAdmin) # new
admin.site.register(Comment) # new
