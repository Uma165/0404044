# Generated by Django 5.0 on 2024-03-15 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appeal',
            name='description',
        ),
        migrations.AlterField(
            model_name='appeal',
            name='type',
            field=models.CharField(choices=[('Культура', 'Культура'), ('Лунная терраса', 'Лунная терраса'), ('8 марта', '8 марта'), ('Дубовый', 'Дубовый'), ('Тайный сад', 'Тайный сад'), ('Два романтика', 'Два романтика')], max_length=128, verbose_name='Стол'),
        ),
    ]
