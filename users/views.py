import random

from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class UsersListView(ListView):
    """
    Класс контроллер список пользователей.
    """

    model = User


class UsersCreateView(CreateView):
    """
    Класс контроллер регистрация пользователя.
    """

    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:verify")

    def form_valid(self, form):
        user = form.save()
        current_site = self.request.get_host()
        ver_code = "".join([str(random.randint(1, 9)) for _ in range(4)])
        user.ver_code = ver_code
        user.is_active = False
        user.save()
        send_mail(
            subject="Верификация",
            message=f"код для входа: {ver_code}\n в {current_site}/users/verify",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


class UsersDetailView(DetailView):
    """
    Класс контроллер просмотра пользователя.
    """

    model = User


class UsersUpdateView(UpdateView):
    """
    Класс контроллер обновления пользователя.
    """

    model = User


class UsersProfileView(UpdateView):
    """
    Класс контроллер обновления пользователя.
    """

    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user


class UsersDeleteView(DeleteView):
    """
    Класс контроллер удаления данных пользователя.
    """

    model = User


class Verify(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "users/verification.html")

    def post(self, request, *args, **kwargs):
        code = request.POST.get("ver_code")
        user = get_object_or_404(User, ver_code=code)

        if not user.is_active:
            user.is_active = True
            user.save()
            return redirect("users:login")
        return redirect("/")
