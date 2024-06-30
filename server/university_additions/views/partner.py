from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from university_additions.models import Partner
from university_additions.serializers.partner import PartnerSerializer


@extend_schema(tags=['Partners'])
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
