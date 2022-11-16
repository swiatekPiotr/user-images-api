from django.db import models
from django.conf import settings
from versatileimagefield.fields import VersatileImageField, PPOIField


class Picture(models.Model):
    class Meta:
        ordering = ('-date',)
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    photo = VersatileImageField('Photo', upload_to='uploads/', ppoi_field='photo_ppoi')
    photo_ppoi = PPOIField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title, self.date
