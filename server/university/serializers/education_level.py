from rest_framework import serializers

from university.models.education_level import EducationLevel


class EducationLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = EducationLevel
        fields = '__all__'
