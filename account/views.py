from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm


# Create your views here.


def signup_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()


	else:
		form = RegisterForm()

	context = {'form' : form}
	return render(request, 'account/register.html', context)





















