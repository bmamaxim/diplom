import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from config import settings
from employee.models import Employee
from employee.service import examination, time_processing, time_minimum
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
    Класс контроллер записи на прием
    выбор даты записи.
    """

    model = SignUp
    form_class = SignUpForm
    success_url = reverse_lazy("service:update-signup")

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


def sign_up(request, pk: int):
    """
    Функция записи к специалисту.
    :param request: dict
    :param pk: int
    :return:
    """
    time_list = [
        datetime.time(hour=8).strftime("%H:%M:%S"),
        datetime.time(hour=9).strftime("%H:%M:%S"),
        datetime.time(hour=10).strftime("%H:%M:%S"),
        datetime.time(hour=11).strftime("%H:%M:%S"),
        datetime.time(hour=13).strftime("%H:%M:%S"),
        datetime.time(hour=14).strftime("%H:%M:%S"),
        datetime.time(hour=15).strftime("%H:%M:%S"),
        datetime.time(hour=16).strftime("%H:%M:%S"),
    ]
    user = request.user
    employee = Employee.objects.filter(pk=pk).first()
    date_max = settings.TODAY + datetime.timedelta(days=7)
    print(date_max.time().strftime("%H:%M:%S"))
    if request.GET.get("date") is None:
        context = {
            "step": "Выберите дату записи",
            "user": user,
            "employee": employee,
            "date_min": settings.TODAY.strftime("%Y-%m-%d"),
            "date_max": date_max.strftime("%Y-%m-%d"),
            "step_1": True
        }
        return render(request, "service/sign_up.html", context)
    else:
        date = request.GET.get("date")
        data = SignUp.objects.filter(employee=employee).all()
        queryset = examination(date, data)
        time = time_processing(queryset, time_list)
        time_filter = time_minimum(time, date)
        context = {
            "step": "Выерите время записи",
            "user": user,
            "employee": employee,
            "day": date,
            "time_list": time_filter,
        }
        return render(request, "service/sign_up.html", context)


def sign_up_info(request, pk: int):
    """
    Функция записывает данные по записи к специалисту.
    :param request: dict
    :param pk: int
    :return:
    """
    if request.method == "POST":
        user = request.user
        employee = Employee.objects.filter(pk=pk).first()
        date = request.POST.get("date")
        time = request.POST.get("time")
        application = SignUp(
            user=user,
            employee=employee,
            date=date,
            time=time
        )
        application.save()
        return render(request, "service/sign_up_info.html",
                      {
                          "user": user,
                          "employee": employee,
                          "date": date,
                          "time": time
                      }
                      )
    else:
        return render(request, "service/sign_up_info.html")
