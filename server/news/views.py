from django.utils import translation
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer

@extend_schema(tags=['News'])
class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Post.objects.filter(status='active')
