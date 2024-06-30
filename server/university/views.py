from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from university.models.education_level import EducationLevel
from university.models.faculty import Faculty
from university.models.partner import Partner
from university.models.program import Program
from university.serializers.education_level import EducationLevelSerializer
from university.serializers.faculty import FacultySerializer
from university.serializers.partner import PartnerSerializer
from university.serializers.program import ProgramSerializer

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

    def get_queryset(self):
        return EducationLevel.objects.all()

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


@extend_schema(tags=['Partner'])
@extend_schema_view(
    list=extend_schema(
        summary='Получить список партнеров'
    ),
    retrieve=extend_schema(
        summary='Получение детальной информации о партнере'
    )
)
class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PartnerSerializer

    def get_queryset(self):
        return Partner.objects.all()