# Generated by Django 2.0 on 2018-12-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video_or_Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_video', models.ImageField(blank=True, null=True, upload_to='profile_videos/%Y/%m/%d')),
                ('main_photo', models.ImageField(blank=True, null=True, upload_to='profile_photo/%Y/%m/%d')),
            ],
        ),
    ]
