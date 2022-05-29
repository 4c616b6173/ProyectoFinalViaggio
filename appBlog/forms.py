from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(forms.Form):
    name = forms.CharField()
    lastname = forms.CharField()
    mail = forms.EmailField()
    event = forms.CharField()

class StudentForm(forms.Form):
    name = forms.CharField()
    lastname = forms.CharField()
    mail = forms.EmailField()
    age = forms.IntegerField()

class CourseForm(forms.Form):
    name = forms.CharField()
    code = forms.IntegerField()
    duration = forms.IntegerField()

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']