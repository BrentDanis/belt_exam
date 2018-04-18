from __future__ import unicode_literals
from django.db import models
from django import forms

#adding data base structure (think excel headers)

class Users(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.EmailField()
	password=models.CharField(max_length=255)
	def __str__(self):
		return "<Users object: {} {}>".format(self.first_name, self.last_name)
