# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


#from django.template.loader import get_template
# Create your views here.

def home(request):
	template = 'home.html'
	context = locals()
	return render(request,template,context)
