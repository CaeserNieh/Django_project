# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	bio = models.TextField(max_length=500,blank=True)
	location = models.CharField(max_length=30,blank=True)
	birth_date = models.DateField(null=True,blank=True)

	def __unicode__(self):
		return self.user.username



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




class Post(models.Model):
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)
	
	class Meta:
		ordering = ('-pub_date',)
	
	def __unicode__(self):
		return self.title


class Read_page(models.Model):

	class Meta:
		permissions = (
			("can_read","Can Read Page"),
		)


class userpage(models.Model):

	class Meta:
		permissions = (
			("can_read","User can read this Page")
		)