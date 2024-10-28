from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display = ("id", "user", "content", "created_at", "updated_at")
    list_display = ('id', 'user', 'content', 'created_at', 'updated_at', 'likes_count', 'dislikes_count')
    list_display_links = ('id', 'user')
    list_filter = ('user', 'created_at', 'updated_at')
    search_fields = ('user', 'content')
    list_per_page = 10

    def __str__(self):
        return self.content[:50]  # Retorna os primeiros 50 caracteres do conteúdo

    """ def get_likes_count(self, obj):
        return (
            obj.likes.count()
        )  # Supondo que você tenha uma relação reversa definida no modelo Like
    get_likes_count.short_description = "Likes"  # Rótulo personalizado
    def get_likes_count(self, obj):
        return obj.likes.count()  # Supondo que você tenha uma relação reversa definida no modelo Like
 """


class Meta:
    ordering = ["-created_at"]
    display = ["id", "user", "content", "created_at", "updated_at"]
