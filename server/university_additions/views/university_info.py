from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, generics

from university_additions.models.university_info import UniversityInfo
from university_additions.serializers.university_info import UniversityInfoSerializer

@extend_schema(tags=['University Info'])
@extend_schema_view(
    retrieve=extend_schema(
        summary='Получить информацию об университете по id=1'
    ),
)
class UniversityInfoViewSet(viewsets.GenericViewSet,
                            generics.RetrieveAPIView):
    queryset = UniversityInfo.objects.all()
    serializer_class = UniversityInfoSerializer
