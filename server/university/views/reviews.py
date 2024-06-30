from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from university.models.reviews import StudentReview, StudentSpeak
from university.serializers.reviews import StudentReviewSerializer, StudentSpeakSerializer


@extend_schema(tags=['Reviews'])
@extend_schema_view(
    list=extend_schema(
        summary='Получить список отзывов от студентов'
    ),
)
class StudentReviewViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StudentReviewSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('faculty', 'education_level')

    def get_queryset(self):
        return StudentReview.objects.all()



@extend_schema(tags=['Reviews'])
@extend_schema_view(
    list=extend_schema(
        summary='Получить список отзывов от студентов'
    ),
)
class StudentSpeakViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StudentSpeakSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('faculty', 'education_level')

    def get_queryset(self):
        return StudentSpeak.objects.all()
