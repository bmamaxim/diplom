from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    """
    Форма регистрации пользователя.
    """

    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email", "tg_id")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget = forms.HiddenInput()
        for fild_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.fields["password"].widget = forms.HiddenInput()


class UserCreateForm(forms.ModelForm):
    """

    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
