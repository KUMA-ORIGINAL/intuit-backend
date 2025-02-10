from rest_framework import serializers

from .models import Post, Category, Image, File, Event


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'title', 'image')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'title', 'file')


class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'status', 'title', 'slug', 'description', 'date', 'banner',
            'categories', 'images', 'files'
        )
        read_only_fields = ('slug',)


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            'id', 'status', 'title', 'slug', 'description', 'created_at', 'banner'
        )
        read_only_fields = ('slug',)
