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


class PostListSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'slug', 'date', 'banner', 'categories',
        )
        read_only_fields = ('slug',)


class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'slug', 'description', 'date', 'banner',
            'categories', 'images', 'files'
        )
        read_only_fields = ('slug',)


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('status', 'title', 'slug', 'description', 'created_at', 'banner', 'link')
        read_only_fields = ('slug', 'created_at')