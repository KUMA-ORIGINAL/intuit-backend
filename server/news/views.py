from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Post, Event
from .serializers import PostSerializer, EventSerializer


class PostPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 100

@extend_schema(tags=['News'])
class PostViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('faculty',)
    serializer_class = PostSerializer
    lookup_field = 'slug'
    pagination_class = PostPagination

    def get_queryset(self):
        return Post.objects.filter(status='active')


@extend_schema(tags=['Events'])
class EventViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('faculty',)
    serializer_class = EventSerializer
    lookup_field = 'slug'
    pagination_class = PostPagination

    def get_queryset(self):
        return Event.objects.filter(status='active')
