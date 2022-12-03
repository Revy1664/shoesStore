from django.db import models
from slugify import slugify

class Brand(models.Model):
    slug = models.SlugField(null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='Название')
    logo = models.ImageField(upload_to='logos/', default='static/images/default_for_brand.jpg', verbose_name='Логотип')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'