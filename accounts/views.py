
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import  Member

from .serializers import (

    MemberSerializer


)

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    pagination_class = LargeResultsSetPagination
