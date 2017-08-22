
from django import forms
from mainsite import models
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import UserProfile

from django.contrib.auth.forms import UserCreationForm

'''
class ProfileForm(forms.ModelForm):
	class Meta:
		model = models.Profile
		fields = ['height','male','website']

	def __init__(self,*args,**kwargs):
		super(ProfileForm,self).__init__(*args,**kwargs)
		self.fields['height'].label = "cm"
		self.fields['male'].label = "boy"
		self.fields['website'].label = 'website'
'''


class LoginForm(forms.Form):
	username = forms.CharField(label="Name", max_length=10)
	password = forms.CharField(label="Password",widget=forms.PasswordInput())


class SignupForm(forms.Form):
	first_name = forms.CharField(label="First Name", max_length=30)
	last_name = forms.CharField(label="Last Name", max_length=30)
	email = forms.EmailField(max_length=254,help_text="Required Inform a valid email address")
	phone = forms.CharField(label="Phone", max_length=50)
	city = forms.CharField(label="City",max_length = 50)
	username = forms.CharField(label="username",max_length=30)
	password = forms.CharField(label="Password",widget=forms.PasswordInput()) 
	#confirm_password = forms.CharField(label="Confirm Passwords",widget=forms.PasswordInput())
	def signup(self,request,user):
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.phone = self.cleaned_data['phone']
		user.city = self.cleaned_data['city']
		user.email = self.cleaned_data['email']
		user.username = self.cleaned_data['username']
		user.password = self.cleaned_data['password']
		#user.confirm_password=self.cleaned_data['confirm_password']
		print(user)
		user.save()

class model_form(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('first_name','last_name','username','number','city','password1','password2','email')



class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30,required=False,help_text="Optional.")
	last_name = forms.CharField(max_length = 30,required=False,help_text="Optional.")
	email = forms.EmailField(max_length=254,help_text="Required Inform a valid email address")
	
	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2',)



'''
username = forms.CharField(label="username",max_length=30)
	password = forms.CharField(label="Password",widget=forms.PasswordInput()) 
	confirm_password = forms.CharField(label="Confirm Passwords",widget=forms.PasswordInput())
	user.username = self.cleaned_data['username']
		user.password = self.cleaned_data['password']
		user.confirm_password=self.cleaned_data['confirm_password']
'''