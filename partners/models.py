from django.db import models

# Create your models here.


class Partners(models.Model):
    logo = models.ImageField(upload_to='partners/%Y/%m/%d', null=True, blank=False)
    link = models.CharField(max_length=120, db_index=True, default=0, blank=True)


    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'