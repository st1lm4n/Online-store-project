from django import forms
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import UpdateView

from .forms import UserProfileForm
from .forms import UserRegisterForm
from .models import User


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)

        # Отправка приветственного письма
        send_mail(
            subject='Добро пожаловать в наш магазин!',
            message=f'Приветствуем, {user.email}! Вы успешно зарегистрировались в нашем магазине.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return response


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'})
    )


class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'
    next_page = 'home'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/login/'
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
