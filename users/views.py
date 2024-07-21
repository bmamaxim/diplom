from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

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


class UsersDeleteView(DeleteView):
    """
    Класс контроллер удаления данных пользователя.
    """

    model = User
