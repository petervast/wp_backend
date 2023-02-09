from django.contrib import admin
from .models import Project, ProjectDeadline, ProjectHour, ProjectMember

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectDeadline)
admin.site.register(ProjectHour)
admin.site.register(ProjectMember)