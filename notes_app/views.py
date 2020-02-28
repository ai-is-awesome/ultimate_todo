from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.urls import reverse


# Create your views here.





def index(request):
	context = {}
	if request.method == 'POST':
		form = TaskForm(request.POST)

		if form.is_valid():
			form.save()
		else:
			context["invalid_form"] = True
		return redirect(reverse('index'))

	else:
		context["not_post"] = True

	tasks = Task.objects.all()
	form = TaskForm()




	context["tasks"] = tasks
	context["form"] = form



	return render(request, 'notes_app/index.html', context)










def update(request, pk):
	context = {}

	if request.method == 'POST':
		task = Task.objects.get(id = pk)

		form = TaskForm(request.POST,instance = task)
		if form.is_valid():
			form.save()
		





	task = Task.objects.get(id = pk)
	form = TaskForm(instance = task)

	context["task"] = task
	context["form"] = form


	return render(request, 'notes_app/task_update.html', context)



def delete_task(request, pk):
	task = Task.objects.get(id = pk)
	task.delete()

	return redirect(reverse('index'))











