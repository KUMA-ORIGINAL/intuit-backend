from rest_framework import serializers

from university_additions.models.reviews import StudentReview, StudentSpeak


class StudentReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentReview
        fields = '__all__'


class StudentSpeakSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentSpeak
        fields = '__all__'
