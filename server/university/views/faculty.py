from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from university.models import Faculty
from university.serializers.faculty import FacultySerializer


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
    serializer_class = FacultySerializer

    def get_queryset(self):
        return Faculty.objects.all()
