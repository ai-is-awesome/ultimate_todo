from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.




class User(AbstractBaseUser):

	
	email = models.EmailField(
		verbose_name = 'email address',
		max_length = 255, 
		unique = True)

	active = models.BooleanField(default = True)
	staff = models.BooleanField(deafault = False)

	admin = models.BooleanField(default = False)

	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = []



	def get_full_name(self):

		return self.email

	def get_short_name(self):

		return self.email

	def __str__(self):

		return self.email



	def has_perm(self,perm, obj = None):
		"Does the user have a specified permission"

		#Simplest possible answer : Yes, always

		return True


	def has_module_perms(self, app_label):
		return True


	@property
	def is_staff(self):
		return self.staff


	@property
	def is_admin(self):
		return self.admin
	














