from rest_framework import serializers

from ..models import PageItem, PageItems

class PageItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PageItems
        fields = ('title', 'description', 'cover', 'link', 'is_external')


class PageItemSerializer(serializers.ModelSerializer):
    items = PageItemsSerializer(many=True, read_only=True)

    class Meta:
        model = PageItem
        fields = ('title', 'slug', 'cover', 'description', 'items')
