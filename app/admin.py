from django.contrib import admin
from .models import TaskList
from .models import Task

admin.site.register(Task)
admin.site.register(TaskList)