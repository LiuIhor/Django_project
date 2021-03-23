from django import forms
from main.models import User, Profile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('middle_name', 'phone')

class UserLoginForm(AuthenticationForm):
    username =  forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class':'form-control'}))


