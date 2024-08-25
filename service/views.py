import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
from employee.service import (
    time_processing,
    time_minimum,
    sign_up_time,
)
from service.forms import ServiceForm, SignUpForm
from service.models import Service, SignUp


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



class ServiceCreateView(UserPassesTestMixin, CreateView):
    """
    Класс контроллер страницы создания услуги.
    """

    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy("service:home")

    def test_func(self):
        if self.request.user.has_perm("create_service"):
            return True
        return self.handle_no_permission()


class ServiceUpdateView(UserPassesTestMixin, UpdateView):
    """
    Класс контроллер изменения сервиса.
    """

    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy("service:home")

    def test_func(self):
        if self.request.user.has_perm("update_service"):
            return True
        return self.handle_no_permission()


class ServiceDetailView(LoginRequiredMixin, DetailView):
    """
    Класс контроллер просмотра подробностей сервиса.
    """

    model = Service
    template_name = "service/detail.html"


class ServiceDeleteView(UserPassesTestMixin, DeleteView):
    """
    Класс контроллер удаления сервиса.
    """

    model = Service
    success_url = reverse_lazy("service:home")

    def test_func(self):
        if self.request.user.has_perm("delete_service"):
            return True
        return self.handle_no_permission()


class SignUpCreateView(UserPassesTestMixin, CreateView):
    """
    Класс контроллер записи на прием
    выбор даты записи.
    """

    model = SignUp
    form_class = SignUpForm
    success_url = reverse_lazy("service:update-signup")
    permission_required = 'service.create_signup'

    def test_func(self):
        if self.request.user.has_perm('service.add_signup'):
            return True
        return self.handle_no_permission()


class SignUpUpdateView(UserPassesTestMixin, UpdateView):
    """
    Класс контроллер изменения записи на прием.
    """

    model = SignUp
    form_class = SignUpForm
    success_url = reverse_lazy("service:list-signup")

    def test_func(self):
        if self.request.user.has_perm("service.change_signup"):
            return True
        return self.handle_no_permission()


class SignUpListView(LoginRequiredMixin, ListView):
    """
    Класс контроллер списка записей на прием.
    """

    model = SignUp

    def get_queryset(self):
        if self.request.user.groups.filter(name="registry"):
            return SignUp.objects.all()
        return SignUp.objects.filter(user=self.request.user)


class SignUpDeleteView(UserPassesTestMixin, DeleteView):
    """
    Класс контроллер удаления записи на прием.
    """

    model = SignUp
    success_url = reverse_lazy("service:list-signup")

    def test_func(self):
        if self.request.user.groups.filter(name="registry"):
            return True


@login_required
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
    # вытаскиваем первую запись сотрудника по id.
    employee = Employee.objects.filter(pk=pk).first()
    date_max = settings.TODAY + datetime.timedelta(days=7)
    if request.GET.get("date") is None:
        context = {
            "step": "Выберите дату записи",
            "user": user,
            "employee": employee,
            "date_min": settings.TODAY.strftime("%Y-%m-%d"),
            "date_max": date_max.strftime("%Y-%m-%d"),
            "step_1": True,
        }
        return render(request, "service/sign_up.html", context)
    else:
        date = request.GET.get("date")
        # вытаскиваем из базы все записи пользователя.
        sign = SignUp.objects.filter(user=user).all()
        # фильтруем записи по значению сотрудника - employee.
        doctors = sign.filter(employee=employee)
        # фильтруем записи к врачу по дате.
        data_sign = doctors.filter(date=date)
        if data_sign:
            context = {
                "title": "Вы уже записаны к этому врачу",
                "doctor": employee,
                "date": date,
                "you_sign": data_sign,
            }
            return render(request, "service/answer.html", context)
        else:
            data_sign = SignUp.objects.filter(employee=employee).all()
            # examination(date, data_sign) не актуальная проверка, но это не точно
            queryset = data_sign.filter(date=date)
            time = time_processing(queryset, time_list)
            time_filter = time_minimum(time, date)
            filter_date_time = sign.filter(date=date)
            lust_time = sign_up_time(filter_date_time, time_filter)
            context = {
                "step": "Выерите время записи",
                "user": user,
                "employee": employee,
                "day": date,
                "time_list": lust_time,
            }
            return render(request, "service/sign_up.html", context)


@login_required
def sign_up_info(request, pk: int):
    """
    Функция записывает данные по записи к специалисту.
    :param request: dict
    :param pk: int
    :return:
    """
    if request.method == "POST":
        user = request.user
        # вытаскиваем первую запись сотрудника по id.
        employee = Employee.objects.filter(pk=pk).first()
        date = request.POST.get("date")
        time = request.POST.get("time")
        application = SignUp(user=user, employee=employee, date=date, time=time)
        query = SignUp.objects.filter(
            user=user, employee=employee, date=date, time=time
        ).first()
        if query:
            # выдаем данные по записи при повторной тправке формы.
            return render(
                request,
                "service/sign_up_info.html",
                {"user": user, "employee": employee, "date": date, "time": time},
            )
        else:
            # после проверки формы на существование записи сохраняем с выводом данныых по записи.
            application.save()
            return render(
                request,
                "service/sign_up_info.html",
                {"user": user, "employee": employee, "date": date, "time": time},
            )
    else:
        return render(request, "service/sign_up_info.html")
