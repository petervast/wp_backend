from dataclasses import fields
from rest_framework import serializers
from .models import Project, ProjectMember, ProjectHour
from django.db.models import Q


class ProjectMemberSerializer(serializers.ModelSerializer):
    membername = serializers.CharField(source='member.user.username')
    projectname = serializers.CharField(source='project.name', read_only=True)
    membercolor = serializers.CharField(source='member.color', read_only=True)

    
    class Meta:
        model = ProjectMember
        fields = "__all__"


class ProjectHourSerializer(serializers.ModelSerializer):
    projectname = serializers.CharField(source='project.name', read_only=True)
    membername = serializers.CharField(source='member.user.username', read_only=True)
    

    class Meta:
        model = ProjectHour
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    projectmember = ProjectMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"





class MemberprojectSerializer(serializers.ModelSerializer):
    membername = serializers.CharField(source='member.user.username')
    customer = serializers.CharField(source='project.customer')
    project_hours = serializers.CharField(source='project.project_hours')
    name = serializers.CharField(source='project.name', read_only=True)

    
    class Meta:
        model = ProjectMember
        fields = "__all__"
