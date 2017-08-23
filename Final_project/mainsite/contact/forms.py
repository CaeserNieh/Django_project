from django import forms

class contactForm(forms.Form):
	name = forms.CharField(required=False, max_length=100,help_text='100 characters max.',widget=forms.TextInput(attrs={'placeholder' : 'Name'}))
	subject = forms.CharField(required=False, max_length=100,help_text='100 characters max.',widget=forms.TextInput(attrs={'placeholder' : 'Subject'}))
	email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder' : 'Email'}))
	comment = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder' : 'Message'}))
