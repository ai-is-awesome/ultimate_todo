from django.db import models
from notes.settings import AUTH_USER_MODEL

from django.utils import timezone as tz
# Create your models here.

class Task(models.Model):


	title = models.CharField(max_length = 250)

	body = models.TextField(null = True, blank = True)

	complete = models.BooleanField(default = False)

	created = models.DateTimeField(auto_now_add = True)

	updated = models.DateTimeField(null = True, blank = True)

	author = models.ForeignKey(AUTH_USER_MODEL, on_delete = models.CASCADE,  null = True, blank = True)

	archive = models.BooleanField(default = False)



	def __str__(self):

		return self.title[:50]


	def save(self, *args, **kwargs):

		if self.pk:
			old_model = Task.objects.get(pk = self.pk)
			for i in ('title', 'body',):
				if getattr(old_model, i, None) != getattr(self, i, None):
					self.updated = tz.now()


		else:
			updated = tz.now()

		super(Task, self).save(*args, **kwargs)


class Title(models.Model):

	title = models.CharField(max_length = 70)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	author = models.ForeignKey(AUTH_USER_MODEL, on_delete = models.CASCADE, null = True, blank = True)

	def __str__(self):
		return self.title[:30]


class Item(models.Model):

	title = models.ForeignKey(Title, on_delete = models.CASCADE)
	text = models.CharField(max_length = 70)
	complete = models.BooleanField(default = False)

	def __str__(self):
		return self.text[:30]
