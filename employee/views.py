from django.forms import inlineformset_factory
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
from service.forms import SignUpForm
from service.models import SignUp


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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SignUPFormset = inlineformset_factory(
            Employee, SignUp, form=SignUpForm, extra=1
        )
        if self.request.method == "POST":
            context_data["formset"] = SignUPFormset(self.request.POST)
        else:
            context_data["formset"] = SignUPFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class EmployeeUpdateView(UpdateView):
    """
    Класс контроллер изменить данные сотрудника.
    """

    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy("employee:employees")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SignUpFormset = inlineformset_factory(
            Employee, SignUp, form=SignUpForm, extra=1
        )
        if self.request.method == "POST":
            context_data["formset"] = SignUpFormset(self.request.POST)
        else:
            context_data["formset"] = SignUpFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class EmployeeDeleteView(DeleteView):
    """
    Класс контроллер удаления данных сотрудника.
    """

    model = Employee
