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


class EmployeeCreateView(CreateView):
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


class EmployeeUpdateView(UpdateView):
    """
    Класс контроллер изменить данные сотрудника.
    """

    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy("employee:employees")


class EmployeeDeleteView(DeleteView):
    """
    Класс контроллер удаления данных сотрудника.
    """

    model = Employee
