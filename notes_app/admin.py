from django.contrib import admin
from .models import Task, Item, Title
# Register your models here.


admin.site.register(Task)#, Item)
admin.site.register(Item)
admin.site.register(Title)