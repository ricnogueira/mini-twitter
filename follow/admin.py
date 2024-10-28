from django.contrib import admin
from .models import Follow


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower', 'following', 'created_at')
    list_display_links = ('id', 'follower')
    list_filter = ('follower', 'following', 'created_at')
    search_fields = ('follower', 'following')
    list_per_page = 10
