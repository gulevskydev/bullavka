# Generated by Django 2.0 on 2018-12-07 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffeehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Кофейня',
                'verbose_name_plural': 'Кофейни',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=64, null=True)),
                ('salary', models.IntegerField(default=0)),
                ('workplace', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('timetable', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('conditions', models.TextField(blank=True, default=None, null=True)),
                ('responsibilities', models.TextField(blank=True, default=None, null=True)),
                ('education', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('experience', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('requirements', models.TextField(blank=True, default=None, null=True)),
                ('coffeehouse', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coffeehouses', to='jobs.Coffeehouse')),
            ],
        ),
    ]
