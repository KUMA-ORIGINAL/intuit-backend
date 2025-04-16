from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from university.models import Faculty
from university.serializers.faculty import FacultySerializer, FacultyListSerializer


@extend_schema(tags=['Faculty'])
@extend_schema_view(
    list=extend_schema(
        summary='Получить список факультетов'
    ),
    retrieve=extend_schema(
        summary='Получение детальной информации о факультете'
    )
)
class FacultyViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'slug'

    def get_queryset(self):
        return Faculty.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return FacultyListSerializer
        return FacultySerializer
