from django.views.generic import View
import smtplib
from main.models import Logo
from django.core.mail import BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

class Contacts(View):
    def get(self, request):
        logo = Logo.objects.latest('pk')
        return render(request, 'contacts/contacts.html', context={'logo': logo})

    def post(self, request):
        name = request.POST['firstname']
        tel = request.POST['tel']
        email = request.POST['email']
        message = request.POST['message']

        try:
            mail_user_ = '#####################'
            mail_password_ = '############'
            to = 'Bullavkamoscow@gmail.com'
            sent_from = email
            email_text = 'Subject: {}\n\n{}'.format(name, 'Имя: ' + name +
                                                    '\nНомер телефона: ' + tel + '\nEmail: ' + email
                                                    + '\nСообщение: ' + message).encode('utf-8')

            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(mail_user_, mail_password_)
            server.sendmail(sent_from, to, email_text)
            server.close()
            print('Email sent!')

        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('contacts_url')

