from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from university.models import Program
from university.serializers.program import ProgramSerializer


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
    serializer_class = ProgramSerializer

    def get_queryset(self):
        return Program.objects.all()