# Generated by Django 2.0 on 2018-12-07 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beverage',
            options={'verbose_name': 'Фотография напитка', 'verbose_name_plural': 'Фотографии напитков'},
        ),
        migrations.AlterModelOptions(
            name='interior',
            options={'verbose_name': 'Фотография интерьера', 'verbose_name_plural': 'Фотографии интерьеров'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Фотография продукции', 'verbose_name_plural': 'Фотографии продукции'},
        ),
    ]
