from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))

    # password2 = forms.CharField(label='Повторите пароль', required=False)
    # email = forms.EmailField(required=True, error_messages='ВВеди почту верно')
    # first_name = forms.BooleanField(disabled=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name')
        # fields = '__all__'


'''class MyGemsForm(forms.ModelForm):

    class Meta:
        model = Gem
        fields = ('__all__')


class MyGemsForm(forms.Form): # Форма, не связанная с моделью (нужна будет доп обработка во вьюхе)
    username = forms.SelectMultiple()
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
'''
