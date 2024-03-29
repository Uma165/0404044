# Generated by Django 5.0 on 2024-03-15 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tapls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('сapacity', models.CharField(max_length=60, verbose_name='Вместимость')),
                ('price', models.CharField(max_length=60, verbose_name='Стоимость')),
                ('publish_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
                ('edit_date', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата редактирования')),
                ('image', models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d')),
                ('view', models.CharField(max_length=128, verbose_name='Просмотры')),
            ],
            options={
                'verbose_name': 'Стол',
                'verbose_name_plural': 'Столы',
                'ordering': ('-publish_date', '-edit_date'),
            },
        ),
    ]
