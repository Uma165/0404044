# Generated by Django 5.0 on 2024-03-15 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tapls',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
    ]