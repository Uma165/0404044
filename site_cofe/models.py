from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название кофе')
    description = models.TextField(verbose_name='Описание кофе')
    image = models.ImageField(upload_to='%Y/%m/%d', blank=True, null=True)

    class Meta:
        verbose_name = 'Кофе'
        verbose_name_plural = 'Кофе'
