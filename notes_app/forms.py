from django import forms

from django.forms import ModelForm

from .models import *
from notes.settings import AUTH_USER_MODEL

class TaskForm(forms.ModelForm):
	body = forms.CharField(required = False)
	class Meta:
		model = Task
		fields = '__all__'

	
	def save_model(self, request, instance, form, change):
		user = request.user

		instance = form.save(commit = False)

		if not change or not instance.author:
			instance.author = user

		instance.save()
		return instance

















