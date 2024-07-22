from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, generics

from university_additions.models.user_application import UserApplication
from university_additions.serializers.user_application import UserApplicationSerializer

@extend_schema(tags=['User Application'])
@extend_schema_view(
    post=extend_schema(
        summary='Создание заявки пользователя'
    ),
)
class UserApplicationViewSet(viewsets.GenericViewSet,
                            generics.CreateAPIView):
    queryset = UserApplication.objects.all()
    serializer_class = UserApplicationSerializer
