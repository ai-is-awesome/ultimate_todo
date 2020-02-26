from django.urls import path
from . import views






urlpatterns = [

	path('', views.index, name = 'index'), 
	path('update/', views.update, name = "task_update"), 
	path('delete/<str:pk>', views.delete_task, name = "task_delete"), 



]



