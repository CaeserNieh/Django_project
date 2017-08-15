# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from .forms import contactForm
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.



def contact(request):
	form = contactForm(request.POST or None)
	confirm_message = None

	if form.is_valid():
		print form.cleaned_data['email']
		name =  form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject = form.cleaned_data['subject']
		message = 'Comment : %s   \nFrom %s \n\nEmail From : %s' %(comment , name,form.cleaned_data['email'])
		emailFrom= form.cleaned_data['email']
		emailTo=[settings.EMAIL_HOST_USER]
		send_mail(subject,message,emailFrom,emailTo,fail_silently=True)
		confirm_message = "Thanks for the Message.   We will get right back to you  !!!"
		form = None

	context = {'form' : form, 'confirm_message' : confirm_message}
	template = 'contact.html'
	return render(request,template,context)
