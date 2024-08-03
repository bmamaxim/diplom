from django import forms

from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    """
    Форма модели сотрудника.
    """

    class Meta:
        model = Employee
        fields = "__all__"
