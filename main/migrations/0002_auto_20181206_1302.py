# Generated by Django 2.0 on 2018-12-06 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video_or_photo',
            name='main_video',
            field=models.FileField(blank=True, null=True, upload_to='profile_videos/%Y/%m/%d'),
        ),
    ]
