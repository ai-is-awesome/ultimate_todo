from django import forms

from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from .models import Account



Account = get_user_model()



class RegisterForm(forms.ModelForm):

	password = forms.CharField(widget = forms.PasswordInput)
	password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'username', )


	def clean_email(self):

		email = self.cleaned_data.get('email')
		qs = Account.objects.filter(email = email)
		if qs.exists():
			raise forms.ValidationError("email is taken")

		else:
			return email

	
	def clean_password2(self):

		password1 = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password1 != password2:
			raise forms.ValidationError("passwords don\'t match. ")

		return self.cleaned_data.get("password2")


class UserAdminCreationForm(forms.ModelForm):
	password1 = forms.CharField(label = "Password", widget = forms.PasswordInput)

	password2 = forms.CharField(label = "Password Confirm pls", widget = forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', )


	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")

		else:
			return password2


	def save(self, commit = True):
		user = super(UserAdminCreationForm, self).save(commit = False)
		if commit:
			user.save()
		return user



class UserAdminChangeForm(forms.ModelForm):

	password = ReadOnlyPasswordHashField()

	class Meta:
		model = Account
		fields = ('email', 'password', 'is_admin', 'is_active')


	def clean_password(self):

		return self.initial("password")



	









