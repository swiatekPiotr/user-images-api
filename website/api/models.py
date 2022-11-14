from django.db import models
from django.conf import settings


class Picture(models.Model):
    class Meta:
        ordering = ('-date',)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='uploads/')
    date = models.DateTimeField(auto_now_add=True)
