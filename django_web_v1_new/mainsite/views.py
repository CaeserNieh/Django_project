# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from datetime import datetime
from django.http import HttpResponse
from .models import Post
from django.template.loader import get_template

from mainsite import forms,models
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from mainsite.forms import SignUpForm
# Create your views here.


def homepage(request):
	template = get_template('index.html')
	posts = Post.objects.all()
	now = datetime.now()
	html = template.render(locals())
	return HttpResponse(html)

def showpost(request,slug):
	template = get_template('post.html')
	try:
		post = Post.objects.get(slug=slug)
		if post != None:
			html = template.render(locals())
			return HttpResponse(html)
	except:
		return redirect('/')


@login_required(login_url='/login/')
def userinfo(request):
	if request.user.is_authenticated():
		username = request.user.username
	user = User.objects.get(username=username)
	try :
		profile = models.Profile.objects.get(user=user)
	except:
		profile = models.Profile(user=user)

	if request.method == 'POST':
		profile_form = forms.ProfileForm(request.POST, instance=profile)
		if profile_form.is_valid():
			messages.add_message(request,messages.INFO,"data store")
			profile_form.save()
			return HttpResponseRedirect('/userinfo')
		else:
			messages.add_message(request,messages.INFO,"modified data")
	else :
		profile_form = forms.ProfileForm()

	template = get_template('userinfo.html')
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)
	return HttpResponse(html)




def login(request):
	if request.user.is_authenticated():
		return redirect('/')
	if request.method == 'POST':
		login_form = forms.LoginForm(request.POST)
		if login_form.is_valid():
			login_name = request.POST['username'].strip()
			login_password = request.POST['password']
			user= authenticate(username=login_name,password=login_password)
			if user is not None:
				if user.is_active:
					auth.login(request,user)
					messages.add_message(request,messages.SUCCESS,"Succed!!!")
					return redirect('/')
				else:
					messages.add_message(request,messages.WARNING,'no activate')
			else:
				messages.add_message(request,messages.WARNING,'fail')
		else:
			messages.add_message(request,messages.INFO,'examine content')
	else:
		login_form = forms.LoginForm()

	template  = get_template('login.html')
	request_context = RequestContext(request)
	request_context.push(locals())
	#html = template.render(request_context)
	return render(request,template,request_context)


def logout(request):
	auth.logout(request)
	messages.add_message(request,messages.INFO,"Logout!")
	return redirect('/')


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username,password=raw_password)
			login(request,user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request,"signup.html",{'form':form} )

