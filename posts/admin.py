from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "create_datetime", "title", "content")
    search_fields = ("id", "title", "username")
    list_filter = ("title", "username")
    list_per_page = 15
    ordering = ("-id",)
