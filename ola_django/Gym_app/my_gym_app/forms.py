
from django import forms
from .models import UserRegistration


class UserRegForm(forms.ModelForm):
      class Meta:
        model = UserRegistration
        fields = ['first_name', 'last_name', 'email', 'password', 'date_of_birth']



      # first_name = forms.CharField(max_length=100)
      # last_name = forms.CharField(max_length=100)
      # email = forms.EmailField()
      # password = forms.CharField(max_length=128)
      # date_of_birth = forms.DateField()
