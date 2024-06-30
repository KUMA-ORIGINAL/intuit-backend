from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from .models import Post
from .serializers import PostReadSerializer

@extend_schema(tags=['News'])
class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostReadSerializer

    def get_queryset(self):
        return Post.objects.filter(status='active')
