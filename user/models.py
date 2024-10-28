from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(unique=True, blank=True, null=True)

    # profile_picture = models.ImageField(upload_to="profiles/", blank=True)

    def __str__(self):
        return self.user.username
