from operator import mod
from django.db import models
from accounts.models import Member
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=124)
    customer = models.CharField(max_length=124, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    project_hours = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    start_week = models.IntegerField(null=True, blank=True)
    end_week = models.IntegerField(null=True, blank=True)
    last_updated = models.DateField(auto_now_add=True)
    projectimage = models.ImageField(upload_to='projects/', blank=True, null=True)


    class Meta:
        unique_together = ['name', 'customer', ]

    def __str__(self):
        return str(self.name)


class ProjectMember(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="projectmember")
    focal_point = models.BooleanField(default=False)

    class Meta:
        unique_together = ['member', 'project', ]

    def __str__(self):
        return str(self.member) + " - " + str(self.project)


class ProjectDeadline(models.Model):
    name = models.CharField(max_length=124)
    date = models.DateField(null=True, blank=True)


class ProjectHour(models.Model):
    hours = models.IntegerField()
    week = models.IntegerField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['member', 'project', 'week']

    def __str__(self):
        return str(self.member) + " in week: " + str(self.week)
