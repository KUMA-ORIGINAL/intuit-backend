from rest_framework import serializers

from university.models.faculty import Faculty


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('id', 'title', 'slug', 'banner', 'subtitle', 'text', 'program_count', 'education_level', 'document_collections')