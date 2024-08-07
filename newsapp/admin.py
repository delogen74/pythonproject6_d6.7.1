from django.contrib import admin
from .models import Post, Author, Category, PostCategory, Comment

class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'dateCreation', 'rating')
    list_filter = ('author', 'dateCreation', 'rating')
    search_fields = ('title', 'text')
    inlines = [PostCategoryInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
