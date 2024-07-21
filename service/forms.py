from django import forms

from service.models import Service


class ServiceForm(forms.ModelForm):
    """
    Класс форма запольнения услуги
    """

    class Meta:
        model = Service
        fields = "__all__"
