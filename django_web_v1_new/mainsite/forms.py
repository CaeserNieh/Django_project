
from django import forms
from mainsite import models
from django.forms import ModelForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):
	class Meta:
		model = models.Profile
		fields = ['height','male','website']

	def __init__(self,*args,**kwargs):
		super(ProfileForm,self).__init__(*args,**kwargs)
		self.fields['height'].label = "cm"
		self.fields['male'].label = "boy"
		self.fields['website'].label = 'website'



class LoginForm(forms.Form):
	username = forms.CharField(label="Name", max_length=10)
	password = forms.CharField(label="Password",widget=forms.PasswordInput())


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30,required=False,help_text="Optional.")
	last_name = forms.CharField(max_length = 30,required=False,help_text="Optional.")
	email = forms.EmailField(max_length=254,help_text="Required Inform a valid email address")
	
	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2',)


