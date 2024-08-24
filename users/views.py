import random

from django.contrib.auth.mixins import UserPassesTestMixin
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


class UsersListView(UserPassesTestMixin, ListView):
    """
    Класс контроллер список пользователей.
    """

    model = User

    def get_queryset(self):
        """
        Позволяем просматривать список пользователей только ркгистратуре.
        :return: queryset
        """
        if self.request.user.groups.filter(name="registry"):
            return User.objects.all()


class UsersCreateView(CreateView):
    """
    Класс контроллер регистрация пользователя.
    """

    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:verify")

    def form_valid(self, form):
        """
        Валидация с отправкой письма с кодом верификации на указаннуюя пользователем почту.
        :param form:
        :return:
        """
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


class UsersDetailView(UserPassesTestMixin, DetailView):
    """
    Класс контроллер просмотра пользователя.
    """

    model = User

    def get_queryset(self):
        """
        Данные по пользователю позволяем просматривать только регистратуре.
        :return: queryset
        """
        if self.request.user.groups.filter(name="registry"):
            return User.objects.all()


class UsersUpdateView(UserPassesTestMixin, UpdateView):
    """
    Класс контроллер обновления пользователя.
    """

    model = User

    def get_queryset(self):
        """
        Изменять данные пользователя разрешаем только регистратуре и самому пользователю.
        :return: queryset
        """
        if self.request.user.groups.filter(name="registry"):
            return User.objects.all()
        return User.objects.filter(user=self.request.user)


class UsersProfileView(UserPassesTestMixin, UpdateView):
    """
    Класс контроллер обновления пользователя.
    """

    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("users:profile")

    def get_queryset(self):
        """
        Работа с профилем пользователя только у самого пользователя.
        :return: queryset
        """


    def get_object(self, queryset=None):
        """
        Предоставляем просмотр пользователю только собственного профиля.
        :param queryset: queryset=None
        :return: queryset
        """
        return self.request.user

    def test_func(self):
        return self.request.user


class UsersDeleteView(UserPassesTestMixin, DeleteView):
    """
    Класс контроллер удаления данных пользователя.
    """

    model = User

    def test_func(self):
        if self.get_object().owner == self.request.user:
            return True
        return self.handle_no_permission()


class Verify(TemplateView):
    """
    Класс верификации пользователя.
    """

    def get(self, request, *args, **kwargs):
        """
        Перенаправляем пользователя на страничку верификации.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return render(request, "users/verification.html")

    def post(self, request, *args, **kwargs):
        """
        Принимаем код от пользователя и переводим в статус "активного пользователя".
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        code = request.POST.get("ver_code")
        user = get_object_or_404(User, ver_code=code)

        if not user.is_active:
            user.is_active = True
            user.save()
            return redirect("users:login")
        return redirect("/")
