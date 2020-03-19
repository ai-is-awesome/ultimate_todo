from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Title, Item
from .forms import TaskForm, TitleForm
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone as tz
# Create your views here.





def index(request):



	context = {}
	html_dict = {True : 'task_complete', False : ''}
	context["html_dict"] = html_dict


	current_user = request.user
	if request.user.is_authenticated:
		tasks = Task.objects.filter(author = current_user, archive = False)
		tasks = tasks.order_by('-updated')
		context["tasks"] = tasks


	else:
		pass

 

	if request.method == 'POST':
		form = TaskForm(request.POST)

		if form.is_valid():
			f = form.save(commit = False)
			f.author = request.user
			f.body = ""
			f.updated = tz.now()
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
		current_user = request.user
		tasks = Task.objects.filter(author = current_user, archive = False)
		tasks = tasks.order_by("-updated")



		#Checking if the current user is the author of the task, if yes then allow him to update his task otherwise redirect him to
		#index
		if len(Task.objects.filter(id = pk)) != 0 and  request.user == Task.objects.filter(id = pk)[0].author:
			if request.method == 'POST':
				task = Task.objects.get(id = pk)
				form = TaskForm(request.POST,instance = task)
				old_title = task.title
				#if form.is_valid():
					#body = form.cleaned_data["body"][:50]
				#title = form.cleaned_data["title"]
				if len(old_title) > 50:
					old_title = old_title[:50]

				messages.success(request, "Task \"%s\" successfully updated" % (old_title))
				form.save()
				return redirect(reverse("index"))

			elif request.method != "POST":
				try:
					task = Task.objects.get(id = pk)
					form = TaskForm(instance = task)
					context["task"] = task
					context["form"] = form
					context["tasks"] = tasks
					return render(request, 'notes_app/task_update.html', context)


				except:
					error_message  ='The following update page does\'nt exist'

					return render(request, 'notes_app/index.html')


		else:

			return redirect(reverse('index'))


	elif not request.user.is_authenticated:
		return redirect(reverse(index))

	

	return render(request, 'notes_app/task_update.html', context)



def archive_task(request, pk):

	try:
		#If someone clicks on the delete task link, then archive the task and redirect
		user = request.user
		author = Task.objects.get(id = pk).author
		if user == author:
			task = Task.objects.get(id = pk)
			task.archive = True
			task.save()
			messages.warning(request, "Task \"%s  \" archived" % (task.title))
			return redirect(reverse('index'))


	except:
		pass
		

	
	

	#If someone visits the archive_task view(ie doesn't click on the delete button but just visits the page) then
	# show all the archive tasks to the user

	#tasks = Task.objects.filter(archive = True)
	#context = {'tasks' :tasks}
	#return render(request, 'notes_app/archive.html', context)
	


def show_archives(request):
	context = {}
	if request.user.is_authenticated:
		current_user = request.user
	else:
		current_user = None
		return redirect(reverse(index))

	tasks = Task.objects.filter(archive = True, author = current_user)
	tasks = tasks.order_by('-updated')

	#If no tasks, then tell user no tasks are deleted
	if len(tasks) == 0:
		no_archives = True
		context["no_archives"] = no_archives


	context["tasks"] =tasks
	return render(request, 'notes_app/archive.html', context)






def restore_archive(request, pk):
	try:
		current_user = request.user
		author = Task.objects.get(id = pk).author
		if current_user == author:
			task = Task.objects.get(id = pk)
			task.archive = False
			task.save()
			messages.success(request, 'Task \"%s\" restored. ' % (task.title))

		return redirect(reverse('archives'))



	except:
		return redirect(reverse('index'))



def delete_archive(request, pk):
	try:
		current_user = request.user
		author = Task.objects.get(id = pk).author
		if current_user == author:
			task = Task.objects.get(id = pk)
			title = task.title
			task.delete()
			messages.warning(request, "Task %s deleted permanently. " % (title))
			return redirect(reverse('archives'))

		
		


	except:
		messages.warning(request, 'Unable to delete Task. ')
		return redirect(reverse('archives'))

	
def update_complete_field(request, pk):
	try:
		current_user = request.user
		author = Task.objects.get(id = pk).author
		if current_user == author:
			task = Task.objects.get(id = pk)
			task.complete = not task.complete
			task.save()
			return redirect(reverse(index))



	except:
		pass

	return redirect(reverse(index))


def checklists_view(request):
	checklist_titles = Title.objects.all()
	context = {}
	context["checklist_titles"] = checklist_titles

	return render(request, "notes_app/checklist.html", context)



def create_checklist(request):
	if request.method == 'POST':
		form = TitleForm(request.POST)




def checklist_detail(request, pk):
	title = Title.objects.get(id = pk)
	items = title.item_set.all()
	context = {}
	context['title'] = title
	context['items'] = items
	return render(request, "notes_app/checklist_detail.html", context)




