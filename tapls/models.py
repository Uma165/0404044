from django.db import models


class Tapls(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    сapacity = models.CharField(max_length=60, verbose_name='Вместимость')
    price = models.CharField(max_length=60, verbose_name='Стоимость')
    publish_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    edit_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата редактирования')
    image = models.ImageField(upload_to='%Y/%m/%d', blank=True, null=True)
    view = models.CharField(max_length=128, verbose_name='Просмотры')

    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'
        ordering = ('-publish_date', '-edit_date')