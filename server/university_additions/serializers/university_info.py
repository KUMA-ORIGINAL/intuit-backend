from rest_framework import serializers

from ..models import UniversityInfo


class UniversityInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityInfo
        fields = '__all__'
