from django.urls import path
from . import views






urlpatterns = [

	path('', views.index, name = 'index'), 
	path('update/<str:pk>', views.update, name = "task_update"), 
	path('delete/<str:pk>', views.archive_task, name = "task_archive"), 



]



