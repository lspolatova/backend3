from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL


class Category(models.Model):
    title = models.CharField(max_length=50)


class Chat(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(AUTH_USER_MODEL, related_name="author_user", null=True, on_delete=models.SET_NULL)
    members = models.ManyToManyField(AUTH_USER_MODEL, related_name="members_user", null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    channel = models.BooleanField(default=False)


class Files(models.Model):
    path = models.CharField(max_length=200)


class Messages(models.Model):
    chat = models.ForeignKey(Chat, null=True, on_delete=models.SET_NULL)
    sender = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    date_create = models.DateTimeField()
    is_read = models.BooleanField(default=False)
    files = models.ManyToManyField(Files, null=True)

