from django.contrib import admin
from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'created_at')
    list_display_links = ('id', 'user')
    list_filter = ('user', 'post', 'created_at')
    search_fields = ('user', 'post')
    list_per_page = 10

    def __str__(self):
        return f"{self.post.content}: {self.content[:50]}..."  # Exibe o username e os primeiros 50 caracteres do conteúdo
    # def __str__(self):
    #    return self.content[:50]  # Retorna os primeiros 50 caracteres do conteúdo
