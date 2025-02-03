from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from document_pages.models import DocumentPage
from document_pages.serializers import DocumentPageListSerializer, DocumentPageSerializer


@extend_schema(tags=['Document Pages'])
class DocumentPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DocumentPage.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return DocumentPageListSerializer
        return DocumentPageSerializer
