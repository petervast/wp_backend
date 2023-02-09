
from urllib import response
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Project, ProjectMember, ProjectHour
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import (
    ProjectSerializer,
    ProjectMemberSerializer,
    ProjectHourSerializer,
    MemberprojectSerializer

)
from django_filters.rest_framework import DjangoFilterBackend
import django_filters


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ProjectFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='exact')
    customer = django_filters.CharFilter(
        field_name='customer', lookup_expr='exact')
    projectmember = django_filters.CharFilter(
        field_name='projectmember__id', lookup_expr='exact')

    class Meta:
        model = Project
        fields = ["name", "customer", "projectmember"]


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['project', 'shop']


class ProjectMemberFilter(django_filters.FilterSet):
    projectname = django_filters.CharFilter(
        field_name='project__name', lookup_expr='exact')
    membername = django_filters.CharFilter(
        field_name='member__user__username', lookup_expr='exact')
    member = django_filters.CharFilter(
        field_name='member__user', lookup_expr='exact')
    project = django_filters.CharFilter(
        field_name='project', lookup_expr='exact')

    class Meta:
        model = ProjectMember
        fields = "__all__"


class ProjectMemberViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectMemberSerializer
    queryset = ProjectMember.objects.all()
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filter_class = ProjectMemberFilter


class ProjectHourFilter(django_filters.FilterSet):
    projectname = django_filters.CharFilter(
        field_name='project__name', lookup_expr='exact')
    membername = django_filters.CharFilter(
        field_name='member__user__username', lookup_expr='exact')
    member = django_filters.CharFilter(
        field_name='member__user', lookup_expr='exact')
    project = django_filters.CharFilter(
        field_name='project', lookup_expr='exact')

    class Meta:
        model = ProjectHour
        fields = "__all__"


class ProjectHourViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectHourSerializer
    queryset = ProjectHour.objects.all()
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filter_class = ProjectHourFilter


@api_view(["get"])
def memberhour(request):

    hours = ProjectHour.objects.values("week", "member").order_by(
        "week").order_by("member").annotate(weekhours=Sum("hours"))

    return Response(hours)





class Memberhours(APIView):

    def get(self, request, format=None):
        querydict = request.GET
        if querydict:
            membername = querydict.dict()["membername"]
            hours = ProjectHour.objects.filter(member__user__username=membername).values("week", "project__name").order_by("week").order_by("member").annotate(weekhours=Sum("hours"))
        else:
            hours = ProjectHour.objects.values("week", "member").order_by("week").order_by("member", "project__name").annotate(weekhours=Sum("hours"))

        return Response(hours)



class MemberProjects(APIView):

    def get(self, request, format=None):

        querydict = request.GET
        if querydict:
            membername = querydict.dict()["membername"]
            print(membername)
            projects = [projectmember.project for projectmember in ProjectMember.objects.filter( member__user__username=membername)]
        else:
            projects = Project.objects.all()

        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

