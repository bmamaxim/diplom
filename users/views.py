from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

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
        if form.is_valid():
            self.object = form.save()
            if form.data.get("need_generate", False):
                self.object.set_passeword(self.object.make_random_password(16))
                self.object.save()

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
