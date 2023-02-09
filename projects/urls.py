from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    ProjectViewSet, 
    ProjectMemberViewSet, 
    ProjectHourViewSet,
    memberhour,
    Memberhours,
    MemberProjects,

)

from rest_framework.routers import DefaultRouter


app_name = 'projects'
router = DefaultRouter()
router.register("api/projects", ProjectViewSet, basename="project"),
router.register("api/projectmembers", ProjectMemberViewSet, basename="projectmember"),
router.register("api/projecthours", ProjectHourViewSet, basename="projecthours"),


urlpatterns =  [
    path('api/test/', memberhour ,name='memberhour'),
    path('api/memberhours/', Memberhours.as_view() ,name='memberhours'),
    path('api/memberprojects/', MemberProjects.as_view(), name='memberprojects'),
]

urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)