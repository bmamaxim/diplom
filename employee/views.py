from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from employee.forms import EmployeeForm
from employee.models import Employee


class EmployeeListView(ListView):
    """
    Класс контроллер списка сотрудников.
    """

    model = Employee

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        if search:
            return Employee.objects.filter(name=search)
        else:
            return Employee.objects.all()


class EmployeeCreateView(UserPassesTestMixin, CreateView):
    """
    Классс контроллер регистрации сотрудников.
    """

    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy("employee:employees")


class EmployeeDetailView(DetailView):
    """
    Класс контроллер просмотра подробностей сотрудника.
    """

    model = Employee
    template_name = "employee/employee_detail.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


class EmployeeUpdateView(UserPassesTestMixin, UpdateView):
    """
    Класс контроллер изменить данные сотрудника.
    """

    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy("employee:employees")


class EmployeeDeleteView(UserPassesTestMixin, DeleteView):
    """
    Класс контроллер удаления данных сотрудника.
    """

    model = Employee
