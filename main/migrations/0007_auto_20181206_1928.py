# Generated by Django 2.0 on 2018-12-06 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20181206_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='photo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='main.Video_or_Photo'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='video',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='main.Video_or_Photo'),
        ),
    ]
