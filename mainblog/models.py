from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(verbose_name="Date Published")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


# Create your models here.
