from django.urls import path
from . import views






urlpatterns = [

	path('', views.index, name = 'index'), 
	path('update/<str:pk>', views.update, name = "task_update"), 
	path('archives/to_archive/<str:pk>', views.archive_task, name = "task_archive"), 
	path('archives', views.show_archives, name = 'archives'), 
	path('archives/restore/<str:pk>', views.restore_archive, name = "restore_archive"), 
	path('archives/delete/<str:pk>', views.delete_archive, name = "delete_archive"), 
	path('update_complete_field/<str:pk>', views.update_complete_field, name = "update_complete_field")




]



