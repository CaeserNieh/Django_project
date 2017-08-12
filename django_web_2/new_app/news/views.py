# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def latestnews(request):
	context = locals()
	template = 'latest_news.html'
	return render(request,template,context)