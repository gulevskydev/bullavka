from django.db import models
from django.utils.text import slugify



def gen_slug(s):
    new_slug = slugify(s, allow_unicode=0)
    return new_slug


class Post(models.Model):
    title = models.CharField(max_length=80, db_index=True)
    # slug = models.SlugField(max_length=80, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    link = models.CharField(max_length=120, db_index=True, default=0, blank=True)
    main_image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='Main image', null=True, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='Detailed image', null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_pub']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Tag(models.Model):
    title = models.CharField(max_length=45)
    # slug = models.SlugField(max_length=45, unique=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'