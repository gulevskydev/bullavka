from .models import *
from django.views.generic import View
from .forms import *
import smtplib
from django.core.mail import BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from main.models import Logo



class Jobs(View):
    def get(self, request):
       coffeehouses = Coffeehouse.objects.all()
       logo = Logo.objects.latest('pk')
       return render(request, 'jobs/job.html', context={'coffeehouses': coffeehouses,
                                                        'logo': logo})



def load_jobnames_jobs(request):
   coffeehouse_id = request.GET.get('coffeehouse')
   jobnames = JobName.objects.filter(coffeehouse_id=coffeehouse_id).order_by('job_name')
   jobs = Job.objects.filter(coffeehouse_id=coffeehouse_id)
   return render(request, 'jobs/jobs_list.html', context={'jobnames': jobnames,
                                                          'jobs':jobs})



class JobFormModel(View):
   def get(self, request):
      logo = Logo.objects.latest('pk')
      form = JobForm()
      coffeehouses = Coffeehouse.objects.all()
      return render(request, 'jobs/job_form.html', context={'form':form,
                                                            'coffeehouses': coffeehouses,
                                                            'logo': logo})

   def post(self, request):
      if request.method == 'POST':
         form = JobForm(request.POST)
         if form.is_valid():

            coffeehouse = form.cleaned_data['coffeehouse'].name
            jobname = form.cleaned_data['jobname'].job_name
            firstname = request.POST['Fname']
            secondname = request.POST['Sname']
            birth_date = request.POST['date']
            citizenship = request.POST['citizenship']
            tel = request.POST['tel']
            email = request.POST['email']
            agreement = request.POST['agree']



            try:
               mail_user_ = '################'
               mail_password_ = '###############'
               to = 'Bullavkamoscow@gmail.com'
               sent_from = email
               email_text = 'Subject: {}\n\n{}'.format(firstname + ' ' + secondname + ' | ' +
                                                       coffeehouse + ' | ' + jobname, 'Кофейня: ' + coffeehouse
                                                       + '\nВакансия: ' + jobname + '\nИмя: ' + firstname +
                                                       '\nФамилия: ' + secondname + '\nEmail: ' + email +
                                                       '\nНомер телефона: ' + tel + '\nГражданство: ' + citizenship
                                                       + '\nДата рождения: ' + birth_date + '\n' + ('Нет, я против этого','Я согласен с тем, '
                                                                                            'что мои персональные данные будут'
                                                                                            ' использоваться компанией.')[agreement == 'agree']).encode('utf-8')

               server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
               server.ehlo()
               server.login(mail_user_, mail_password_)
               server.sendmail(sent_from, to, email_text)
               server.close()
               print('Email sent!')

            except BadHeaderError:
               return HttpResponse('Invalid header found.')
            return redirect('form_url')

      return redirect('form_url')




def load_jobnames(request):
   coffeehouse_id = request.GET.get('coffeehouse')
   jobnames = JobName.objects.filter(coffeehouse_id=coffeehouse_id).order_by('job_name')
   return render(request, 'jobs/coffeehouse_dropdown_list_options.html', context={'jobnames': jobnames})