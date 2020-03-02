from django import forms

from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
	body = forms.CharField(required = False)

	class Meta:
		model = Task
		fields = '__all__'

		









