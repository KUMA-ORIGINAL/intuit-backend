from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from university.models import EducationLevel
from university.serializers.education_level import EducationLevelSerializer, \
    EducationLevelListSerializer


@extend_schema(tags=['Education Level'])
@extend_schema_view(
    list=extend_schema(
        summary='Получить список уровней обучения'
    ),
    retrieve=extend_schema(
        summary='Получение детальной информации об уровне обучения'
    )
)
class EducationLevelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EducationLevelSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return EducationLevel.objects.all()

    def get_serializer_class(self):
        if self.action =='retrieve':
            return EducationLevelSerializer
        return EducationLevelListSerializer
