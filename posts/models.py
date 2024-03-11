from django.db import models


class Post(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30)
    content = models.CharField(verbose_name="Content", max_length=50)
    username = models.CharField(verbose_name="Username", max_length=15)
    create_datetime = models.DateTimeField(auto_now_add=True)
