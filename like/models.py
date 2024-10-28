from django.db import models
from django.core.exceptions import ValidationError


class Like(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    post = models.ForeignKey("post.Post", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "post")

    def clean(self):
        # Impede que um usuário curta seu próprio post
        if self.user == self.post.user:
            raise ValidationError("You cannot like your own post")

    def save(self, *args, **kwargs):
        # Chama o método clean() para validar antes de salvar
        self.clean()
        super(Like, self).save(*args, **kwargs)

        # Update likes count
        self.post.likes_count = self.post.likes_count + 1
        self.post.save()

    def delete(self, *args, **kwargs):
        # Atualiza a contagem de likes ao deletar
        super(Like, self).delete(*args, **kwargs)
        self.post.likes_count = max(0, self.post.likes_count - 1)
        self.post.save()
