from django import forms

from django.forms import ModelForm

from .models import *
from notes.settings import AUTH_USER_MODEL

class TaskForm(forms.ModelForm):
	#body = forms.CharField(required = False)
	class Meta:
		model = Task
		#fields = ['title', 'body']
		fields = ['title', 'body', 'complete']
		





