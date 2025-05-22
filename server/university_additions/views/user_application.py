from django.utils.timezone import localtime
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, generics

from university_additions.models.user_application import UserApplication
from university_additions.serializers.user_application import UserApplicationSerializer
from university_additions.utils import send_telegram_message


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

    def perform_create(self, serializer):
        instance = serializer.save()
        created_at = localtime(instance.created).strftime("%d.%m.%Y %H:%M")
        send_telegram_message(
            f"📝 Новая заявка на обучение:\n\n"
            f"<b>Имя:</b> {instance.user}\n"
            f"<b>Email:</b> {instance.email}\n"
            f"<b>Номер телефона:</b> {instance.phone}\n"
            f"<b>Статус:</b> {instance.get_status_display()}\n"
            f"<b>путь к странице сайте:</b> {instance.slug}\n"
            f"<b>Дата создания заявки:</b> {created_at}\n"
        )
