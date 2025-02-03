from rest_framework import serializers

from document_pages.models import DocumentPage
from .document_collection import DocumentCollectionSerializer


class DocumentPageBaseSerializer(serializers.ModelSerializer):
    document_collections = DocumentCollectionSerializer(many=True, read_only=True)

    class Meta:
        model = DocumentPage
        fields = ('title', 'slug', 'subtitle', 'photo', 'content', 'document_collections')


class DocumentPageSerializer(DocumentPageBaseSerializer):
    pass


class DocumentPageListSerializer(DocumentPageBaseSerializer):

    class Meta(DocumentPageBaseSerializer.Meta):
        fields = ('title', 'slug', 'subtitle', 'photo',)
