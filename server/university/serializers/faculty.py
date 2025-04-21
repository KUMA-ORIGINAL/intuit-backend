from rest_framework import serializers

from document_pages.serializers import DocumentCollectionSerializer
from university.models.faculty import Faculty


class FacultySerializer(serializers.ModelSerializer):
    document_collections = DocumentCollectionSerializer(many=True, read_only=True)

    class Meta:
        model = Faculty
        fields = ('id', 'title', 'slug', 'icon', 'banner', 'subtitle', 'text', 'program_count', 'education_level', 'document_collections')


class FacultyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = ('id', 'title', 'subtitle', 'slug', 'icon', 'program_count')
