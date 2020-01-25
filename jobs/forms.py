from django import forms
from .models import JobName, Job

class JobForm(forms.ModelForm):
   class Meta:
       model = Job
       fields = ('coffeehouse', 'jobname')

   def __init__(self, *args, **kwargs):
       super(JobForm, self).__init__(*args, **kwargs)
       self.fields['jobname'].widget.attrs['class'] = 'js-select3'
       self.fields['coffeehouse'].widget.attrs['class'] = 'js-select2'
       self.fields['jobname'].queryset = JobName.objects.none()




       if 'coffeehouse' in self.data:
           try:
               coffeehouse_id = int(self.data.get('coffeehouse'))

               self.fields['jobname'].queryset = JobName.objects.filter(coffeehouse_id=coffeehouse_id).order_by('job_name')

           except (ValueError, TypeError):
               pass  # invalid input from the client; ignore and fallback to empty City queryset
       elif self.instance.pk:
           self.fields['jobname'].queryset = self.instance.coffeehouse.jobname_set.order_by('job_name')

