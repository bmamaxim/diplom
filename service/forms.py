from django import forms

from service.models import Service, SignUp


class ServiceForm(forms.ModelForm):
    """
    Класс форма запольнения услуги
    """

    class Meta:
        model = Service
        fields = "__all__"


class SignUpForm(forms.ModelForm):
    """
    Класс форма записи к специалисту.
    """

    class Meta:
        model = SignUp
        fields = "__all__"
