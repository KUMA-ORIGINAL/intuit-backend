from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from ..models import PageItem
from ..serializers import PageItemSerializer


@extend_schema(tags=['Page Items'])
@extend_schema_view(
    list=extend_schema(
        summary='Получить список элементов для страниц'
    ),
    retrieve=extend_schema(
        summary='Получение детальной информации о элементах для страницы'
    )
)
class PageItemViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PageItemSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return PageItem.objects.all()