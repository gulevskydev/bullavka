from django.db import models

class Video_or_Photo(models.Model):
    main_video = models.BooleanField(default=False)
    main_photo = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Фото или видео на главной странице'
        verbose_name_plural = 'Фото или видео на главной странице'


class Videos(models.Model):
    video = models.ForeignKey(Video_or_Photo, blank=True, null=True, default=None,
                              on_delete=models.CASCADE, related_name='videos')
    VIDEO = models.FileField(upload_to='profile_videos', null=True, blank=True)
    # PHOTO = models.ImageField(upload_to='profile_photo/%Y/%m/%d', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

class Photos(models.Model):
    photo = models.ForeignKey(Video_or_Photo, blank=True, null=True, default=None,
                              on_delete=models.CASCADE,related_name='photos')
    PHOTO = models.ImageField(upload_to='profile_photo/%Y/%m/%d', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

class Logo(models.Model):
    PHOTO = models.FileField(upload_to='logo/%Y/%m/%d', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипы'