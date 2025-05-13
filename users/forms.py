from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2']


# переопределяем название поля username
class EmailAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'email'


class ProfileForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'about_self', 'birth_date']

        # виджет для удобного ввода даты
        widgets = {'birth_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')}
