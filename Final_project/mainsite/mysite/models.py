# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserProfile(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	username = models.CharField(max_length=200)
	number = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	password1 = models.CharField(max_length=500)
	password2 = models.CharField(max_length=500)
	email = models.EmailField(max_length=200,default="xxx@gmail.com")
	def __unicode__(self):
		return self.username