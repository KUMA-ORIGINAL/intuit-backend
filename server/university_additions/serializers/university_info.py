from rest_framework import serializers

from university_additions.models.university_info import UniversityInfo


class UniversityInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityInfo
        fields = '__all__'
