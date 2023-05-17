from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.title
