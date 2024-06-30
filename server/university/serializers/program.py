from rest_framework import serializers

from university.models.program import Program


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'
