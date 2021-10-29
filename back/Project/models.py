from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    name = models.URLField(
        null=False,
        help_text="User name",
        verbose_name="user_name"
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
