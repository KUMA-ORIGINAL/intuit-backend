from rest_framework import serializers

from university.models import Faculty
from university.models.staff import Staff, Position


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ('id', 'title', 'level')


class StaffSerializer(serializers.ModelSerializer):
    position = PositionSerializer()

    class Meta:
        model = Staff
        fields = ('id', 'name',  'slug', 'position', 'rank', 'status', 'description',
                  'image', 'whatsapp', 'facebook', 'telegram', 'instagram', 'youtube',
                  'curriculum_vitae', 'cv', 'qr_code', 'faculty')
