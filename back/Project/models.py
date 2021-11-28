from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    name = models.CharField(
        null=False,
        help_text="User name",
        verbose_name="user_name",
        max_length=32
    )
    last_name = models.CharField(
        null=False,
        help_text="Last name",
        verbose_name="last_name",
        max_length=32
    )
    age = models.IntegerField(
        null=False,
        help_text="Age",
        verbose_name="age"
    )
    photo = models.CharField(
        max_length=256,
        null=True,
        verbose_name='PhotoPath',
        help_text='The path to the photo'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User info",
        verbose_name="user_info",
        null=True
    )

    # def __str__(self):
    #     return str(self.name)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        app_label = 'Project'


class Likes(models.Model):
    who_give = models.ForeignKey(
        to=User,
        null=False,
        on_delete=models.CASCADE,
        verbose_name='who_give_like',
        help_text='Who give like',
        related_name='who_give_like'
    )
    who_take = models.ForeignKey(
        to=User,
        null=False,
        on_delete=models.CASCADE,
        verbose_name='who_take_like',
        help_text='Who take like',
        related_name='who_take_like'
    )
    hidden = models.BooleanField(
        null=False,
        verbose_name='hidden',
        help_text='Hidden like'
    )

    # def __str__(self):
    #     return str(self.who_give)

    class Meta:
        verbose_name = "Likes"
        verbose_name_plural = "Likes"
        app_label = 'Project'
