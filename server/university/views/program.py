from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from university.models import Program
from university.serializers.program import ProgramSerializer, ProgramListSerializer


@extend_schema(tags=['Program'])
@extend_schema_view(
    list=extend_schema(
        summary='Получить список программ обучения'
    ),
    retrieve=extend_schema(
        summary='Получение детальной информации о программе обучения'
    )
)
class ProgramViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('faculty', 'education_level')
    lookup_field = 'slug'

    def get_queryset(self):
        return Program.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProgramSerializer
        return ProgramListSerializer
