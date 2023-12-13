from django import forms

from .models import User

class CreateUserForm(forms.ModelForm):
    password_confirmation = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password again'}),
    )
    class Meta:
        model = User

        fields = ['first_name', 'last_name', 'nickname', 'password', 'password_confirmation']

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Surname'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }

        labels = {
            'first_name': 'Name',
            'last_name': 'Surname',
            'username': 'Username',
            'password': 'Password',
        }

        help_texts = {
            'username': 'Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.',
            'password': 'Ваш пароль должен содержать как минимум 3 символа.',
        }