from django.utils.timezone import localtime
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, generics

from university_additions.models.user_application import UserApplication
from university_additions.serializers.user_application import UserApplicationSerializer
from university_additions.utils import send_telegram_message, escape_markdown


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
            "📝 *Новая заявка на обучение:*\n\n"
            f"*👤 Имя:* {escape_markdown(instance.user)}\n"
            f"*✉️ Email:* {escape_markdown(instance.email)}\n"
            f"*📞 Телефон:* {escape_markdown(instance.phone)}\n"
            f"📌 *Статус:* {escape_markdown(instance.get_status_display())}\n"
            f"🌐 *Страница:* {escape_markdown(instance.slug)}\n"
            f"🕓 *Дата создания:* {escape_markdown(created_at)}\n"
        )
