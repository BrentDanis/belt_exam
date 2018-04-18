from __future__ import unicode_literals
from django.db import models
from django import forms

#adding data base structure (think excel headers)

class Users(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.EmailField()
	password=models.CharField(max_length=255)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	birthday = models.DateField(auto_now = False, auto_now_add = False, default= '1900-00-00')
	def __str__(self):
		return "<Users object: {} {}>".format(self.first_name, self.last_name)
