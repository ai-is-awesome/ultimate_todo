from django.urls import path
from . import views






urlpatterns = [

	path('', views.index, name = 'index'), 
	path('update/<str:pk>', views.update, name = "task_update"), 
	path('archives/to_archive/<str:pk>', views.archive_task, name = "task_archive"), 
	path('archives', views.show_archives, name = 'archives'), 
	path('archives/restore/<str:pk>', views.restore_archive, name = "restore_archive"), 
	path('archives/delete/<str:pk>', views.delete_archive, name = "delete_archive"), 
	path('update_complete_field/<str:pk>', views.update_complete_field, name = "update_complete_field"), 
	path('checklist/', views.checklists_view, name = "checklists"), 
	path('checklist/title/<str:pk>', views.checklist_detail, name = "checklist_detail"), 
	path('checklist/create', views.create_checklist, name = 'checklist_create'), 
	path('checklist/<str:pk_title>/item/create', views.create_checklist_item, name = 'checklist_item_create'), 
	path('checklist/<str:pk_checklist>/update', views.update_checklist_name, name = 'checklist_name_update'), 
	path('checklist/<str:pk_checklist>/delete', views.delete_checklist, name = 'checklist_delete')




]



