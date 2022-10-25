from django import forms
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import smtplib
import ssl
from django.conf import settings

class SignupForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")



    def send_email(self):
        send_mail(
        'BIENVENUE CHEZ E-COMMERCE',
        'message de Bienvenue aux nouveaux client',
        settings.EMAIL_HOST_USER,
        [self.cleaned_data['email']],
        fail_silently=False,
        )

# class SigninForm(forms.Form):

#     pseudo = forms.CharField(max_length=30)
#     motDepasse1 = forms.CharField(max_length=40)

# class ForgotForm(forms.Form):

#     email = forms.CharField(max_length=100)
#     def send_email(self):
#         send_mail(
#         'RESTAURATION DE MOT DE PASSE',
#         'message de restauration  de mot de passes',
#        ' ecommerce.debug@gmail.com',
#         [self.cleaned_data['email']],
#         fail_silently=False,
#         )

#         # port = settings.EMAIL_PORT
#         # smtp_server = settings.EMAIL_HOST
#         # sender_email = settings.EMAIL_HOST_USER
#         # password = settings.EMAIL_HOST_PASSWORD
#         # receiver_email = self.cleaned_data['email']
#         # subject = 'RESTAURATION DE MOT DE PASSE'
#         # body = 'message de restauration  de mot de passes'
#         # message = 'Subject: {}\n\n{}'.format(subject, body)
#         # context = ssl.create_default_context()
#         # with smtplib.SMTP(smtp_server, port) as server:
#         #             server.ehlo()  # Can be omitted
#         #             server.starttls(context=context)
#         #             server.ehlo()  # Can be omitted
#         #             server.login(sender_email, password)
#         #             server.sendmail(sender_email, receiver_email, message)


# class ConnexionForm(forms.Form):
#     username = forms.CharField(label="Nom d'utilisateur", max_length=30)
#     password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


