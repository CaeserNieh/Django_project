from django import forms
from mysite import models
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import UserProfile

from django.contrib.auth.forms import UserCreationForm



class model_form(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('first_name','last_name','username','password1','password2','email','number','city')
