from django.db import models
from notes.settings import AUTH_USER_MODEL
# Create your models here.





class Task(models.Model):


	title = models.CharField(max_length = 250)

	body = models.TextField(null = True, blank = True)

	complete = models.BooleanField(default = False)

	created = models.DateTimeField(auto_now_add = True)

	updated = models.DateTimeField(auto_now = True,)

	author = models.ForeignKey(AUTH_USER_MODEL, on_delete = models.CASCADE,  null = True, blank = True)






	def __str__(self):

		return self.title[:50]




