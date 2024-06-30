from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from university.models.staff import Staff
from university.serializers.staff import StaffSerializer


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
    serializer_class = StaffSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Staff.objects.all()
