# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	height = models.PositiveIntegerField(default=160)
	male = models.BooleanField(default=False)
	website = models.URLField(null=True)

	def __unicode__(self):
		return self.user.username



class Post(models.Model):
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)
	
	class Meta:
		ordering = ('-pub_date',)
	
	def __unicode__(self):
		return self.title
