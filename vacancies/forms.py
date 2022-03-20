from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset
from vacancies.models import Application, Vacancy


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Войти'))
        self.helper.add_input(Reset('reset', 'Отмена'))

    class Meta:
        model = User


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Создать'))
        self.helper.add_input(Reset('reset', 'Отмена'))

    class Meta:
        model = User

        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )


class ApplicationForm(forms.ModelForm):
    written_username = forms.CharField(max_length=64, label='Вас зовут')
    written_phone = forms.CharField(max_length=15, label='Ваш телефон')
    written_cover_letter = forms.CharField(max_length=5000, widget=forms.Textarea, label='Сопроводительное письмо')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Отправить'))

    class Meta:
        model = Application

        fields = (
            'written_username',
            'written_phone',
            'written_cover_letter',
        )
