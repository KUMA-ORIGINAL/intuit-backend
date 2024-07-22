from rest_framework import serializers

from university_additions.models.user_application import UserApplication


class UserApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserApplication
        fields = ('user', 'phone', 'email', 'slug')
