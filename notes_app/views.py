from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.urls import reverse


# Create your views here.





def index(request):
	context = {}

	current_user = request.user
	if request.user.is_authenticated:
		tasks = Task.objects.filter(author = current_user)
		context["tasks"] = tasks

	else:
		pass



	if request.method == 'POST':
		form = TaskForm(request.POST)

		if form.is_valid():
			f = form.save(commit = False)
			f.author = request.user
			f.save()
			return redirect(reverse('index'))
		else:
			context["invalid_form"] = True
		return redirect(reverse('index'))

	else:
		context["not_post"] = True

	
	form = TaskForm()

	
	context["form"] = form

	return render(request, 'notes_app/index.html', context)










def update(request, pk):
	context = {}


	if request.user.is_authenticated:
		if len(Task.objects.filter(id = pk)) != 0 and  request.user == Task.objects.filter(id = pk)[0].author:
			if request.method == 'POST':
				task = Task.objects.get(id = pk)
				form = TaskForm(request.POST,instance = task)
				if form.is_valid():
					form.save()
				return redirect(reverse("index"))

			elif request.method != "POST":
				try:
					task = Task.objects.get(id = pk)
					form = TaskForm(instance = task)
					context["task"] = task
					context["form"] = form
					return render(request, 'notes_app/task_update.html', context)


				except:
					error_message  ='The following update page does\'nt exist'

					return render(request, 'notes_app/index.html')


		else:
			return redirect(reverse('index'))


	elif not user.is_authenticated:
		return render(request, 'notes_app/index.html')







		



	return render(request, 'notes_app/task_update.html', context)



def delete_task(request, pk):
	task = Task.objects.get(id = pk)
	task.delete()

	return redirect(reverse('index'))











