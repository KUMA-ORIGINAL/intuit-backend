from rest_framework import serializers

from university.models.education_level import EducationLevel


class EducationLevelSerializer(serializers.ModelSerializer):
    admission_eligibility = serializers.SlugRelatedField(many=True,
                                                         read_only=True,
                                                         slug_field='name')

    class Meta:
        model = EducationLevel
        fields = '__all__'
