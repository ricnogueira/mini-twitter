""" from django.db import models
from django.contrib.auth.models import User

 """
""" class Follow(models.Model):
    follower = models.ForeignKey(
        User, related_name="following", on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        User, related_name="followers", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "following")
 """

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def clean(self):
        # Prevents a user from following themselves
        if self.follower == self.following:
            raise ValidationError("You can't follow yourself.")

    def save(self, *args, **kwargs):
        # Chama o método clean() para validar antes de salvar
        self.clean()
        super(Follow, self).save(*args, **kwargs)
