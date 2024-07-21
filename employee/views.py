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


class EmployeeDetailView(DetailView):
    """
    Класс контроллер просмотра подробностей сотрудника.
    """
    model = Employee


class EmployeeUpdateView(UpdateView):
    """
    Класс контроллер изменить данные сотрудника.
    """

    model = Employee


class EmployeeDeleteView(DeleteView):
    """
    Класс контроллер удаления данных сотрудника.
    """

    model = Employee
