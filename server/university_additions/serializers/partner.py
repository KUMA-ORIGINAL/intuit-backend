from rest_framework import serializers

from university_additions.models.partner import Partner


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = '__all__'
