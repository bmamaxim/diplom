from django import forms

from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    """
    Форма модели сотрудника.
    """
    model = Employee

