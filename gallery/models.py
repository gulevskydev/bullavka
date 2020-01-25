from django.db import models


class Gallery(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'

class Interior(models.Model):
    interior = models.ForeignKey(Gallery, blank=True, null=True, default=None,
                              on_delete=models.CASCADE,related_name='interiors')
    photo = models.ImageField(upload_to='interiors/%Y/%m/%d', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    active_on_mobile = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Фотография интерьера'
        verbose_name_plural = 'Фотографии интерьеров'


class Beverage(models.Model):
    beverage = models.ForeignKey(Gallery, blank=True, null=True, default=None,
                              on_delete=models.CASCADE,related_name='beverages')
    photo = models.ImageField(upload_to='beverages/%Y/%m/%d', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    active_on_mobile = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Фотография напитка'
        verbose_name_plural = 'Фотографии напитков'


class Product(models.Model):
    product = models.ForeignKey(Gallery, blank=True, null=True, default=None,
                              on_delete=models.CASCADE,related_name='products')
    photo = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    active_on_mobile = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Фотография продукции'
        verbose_name_plural = 'Фотографии продукции'
