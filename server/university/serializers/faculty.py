from rest_framework import serializers

from university.models.faculty import Faculty


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'