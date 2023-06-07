from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import College, StudentAdmissionForm

class SignUpForm(UserCreationForm):
    CNIC = forms.CharField(max_length=15)
    phone_number = forms.CharField(max_length=15)
    role = forms.ChoiceField(choices=(('admin', 'Admin'), ('college', 'College'), ('student', 'Student')))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'CNIC', 'phone_number', 'role']
