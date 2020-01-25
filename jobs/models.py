from django.db import models


class Coffeehouse(models.Model):
   name = models.CharField(max_length=64, blank=True, null=True, default=None)
   is_active = models.BooleanField(default=True)

   def __str__(self):
       return "%s" % self.name

   class Meta:
       verbose_name = 'Кофейня'
       verbose_name_plural = 'Кофейни'

class JobName(models.Model):
   job_name = models.CharField(max_length=64, null=True, default=None)
   coffeehouse = models.ForeignKey(Coffeehouse, on_delete=models.CASCADE)

   def __str__(self):
       return "%s" % self.job_name

   class Meta:
       verbose_name = 'Название вакансии'
       verbose_name_plural = 'Названия вакансий'


class Job(models.Model):
   coffeehouse = models.ForeignKey(Coffeehouse, on_delete=models.SET_NULL, null=True)
   jobname = models.ForeignKey(JobName, on_delete=models.SET_NULL, null=True)
   salary = models.CharField(max_length=100, blank=True, null=True, default=None)
   workplace = models.CharField(max_length=100, blank=True, null=True, default=None)
   timetable = models.CharField(max_length=100, blank=True, null=True, default=None)
   conditions = models.TextField(blank=True, null=True, default=None)
   responsibilities = models.TextField(blank=True, null=True, default=None)
   education = models.CharField(max_length=100, blank=True, null=True, default=None)
   experience = models.CharField(max_length=100, blank=True, null=True, default=None)
   requirements = models.TextField(blank=True, null=True, default=None)

   class Meta:
       verbose_name = 'Вакансия'
       verbose_name_plural = 'Вакансии'