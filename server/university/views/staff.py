from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, mixins

from university.models.staff import Staff, Position
from university.serializers.staff import StaffSerializer, PositionSerializer


@extend_schema(tags=['Staff'])
@extend_schema_view(
    list=extend_schema(
        summary='Получить список персонала'
    ),
    retrieve=extend_schema(
        summary='Получение детальной персонале'
    )
)
class StaffViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('faculty', 'position')
    serializer_class = StaffSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Staff.objects.all()

@extend_schema(tags=['Staff'])
@extend_schema_view(
    list=extend_schema(
        summary='Получить список должностей'
    ),
)
class PositionViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin):
    serializer_class = PositionSerializer

    def get_queryset(self):
        return Position.objects.all()