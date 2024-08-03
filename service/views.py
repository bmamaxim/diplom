from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from service.forms import ServiceForm
from service.models import Service


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
