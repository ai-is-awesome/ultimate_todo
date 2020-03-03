from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.


def signup_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account created for %s' % (username))
			new_user = authenticate(request, username = username, password = form.cleaned_data.get('password'))
			login(request, new_user)
			
			return redirect('index')
		else:
			form = RegisterForm()
			errors = form.errors


	else:
		form = RegisterForm()

	context = {'form' : form}
	return render(request, 'account/register.html', context)





















