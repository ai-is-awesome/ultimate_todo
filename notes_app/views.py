from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.urls import reverse


# Create your views here.





def index(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()

		return redirect(reverse('index'))

	else:
		tasks = Task.objects.all()
		form = TaskForm()


	form = TaskForm()
	tasks = Task.objects.all()

	context = {
		"tasks" : tasks, 
		"form" : form, 

			}



	return render(request, 'notes_app/index.html', context)










def update(request):

	return render(request, 'notes_app/task_update.html')



def delete_task(request, pk):
	task = Task.objects.get(id = pk)
	pass









