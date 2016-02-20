from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.user.email

class Task(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	isComplete = models.BooleanField(default=False)
	collab1 = models.EmailField(max_length=50)
	collab2 = models.EmailField(max_length=50)
	collab3 = models.EmailField(max_length=50)

	@classmethod
	def create(cls, owner, title):
		task = cls(title=title)
		# do something with the book
		task.owner = owner
		return task
