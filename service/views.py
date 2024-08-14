from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from employee.models import Employee
from service.forms import ServiceForm, SignUpForm
from service.models import Service, SignUp
from users.models import User


class ServiceHomeView(ListView):
    """
    Класс контроллер домашней страницы.
    """

    model = Service
    template_name = "service/home.html"


class ServiceListView(ListView):
    """
    Класс контроллер страницы списка услуг.
    """

    model = Service
    template_name = "service/service_list.html"


class ServiceCreateView(CreateView):
    """
    Класс контроллер страницы создания услуги.
    """

    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy("service:home")


class ServiceUpdateView(UpdateView):
    """
    Класс контроллер изменения сервиса.
    """

    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy("service:home")


class ServiceDetailView(DetailView):
    """
    Класс контроллер просмотра подробностей сервиса.
    """

    model = Service
    template_name = "service/detail.html"


class ServiceDeleteView(DeleteView):
    """
    Класс контроллер удаления сервиса.
    """

    model = Service
    success_url = reverse_lazy("service:home")


class SignUpCreateView(CreateView):
    """
    Класс контроллер записи на прием.
    """

    model = SignUp
    form_class = SignUpForm
    success_url = reverse_lazy("service:list-signup")

    def form_valid(self, form):
        self.object = form.save()
        self.object.employee = Employee.objects.filter(pk=self.kwargs['pk']).first()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class SignUpUpdateView(UpdateView):
    """
    Класс контроллер изменения записи на прием.
    """

    model = SignUp
    form_class = SignUpForm
    success_url = reverse_lazy("service:list-signup")


class SignUpListView(ListView):
    """
    Класс контроллер списка записей на прием.
    """

    model = SignUp


class SignUpDeleteView(DeleteView):
    """
    Класс контроллер удаления записи на прием.
    """

    model = SignUp
    success_url = reverse_lazy("service:list-signup")
