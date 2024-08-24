from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()

            # Отправка приветственного письма
            subject = 'Добро пожаловать на наш Новостной Портал!'
            text = (
                f'{user.username}, добро пожаловать на наш Новостной Портал!\n'
                'Здесь вы найдете последние новости со всего мира.'
            )
            html = (
                f'<b>{user.username}</b>, добро пожаловать на наш Новостной Портал!<br>'
                'Здесь вы найдете последние новости со всего мира.'
            )
            msg = EmailMultiAlternatives(
                subject=subject, body=text, from_email='autotechsupp74@yandex.ru', to=[user.email]
            )
            msg.attach_alternative(html, "text/html")
            msg.send()

        return user
