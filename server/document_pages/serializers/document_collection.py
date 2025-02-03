from rest_framework import serializers

from document_pages.models import DocumentCollection
from .document_collection_item import DocumentCollectionItemSerializer


class DocumentCollectionSerializer(serializers.ModelSerializer):
    document_collection_items = DocumentCollectionItemSerializer(many=True, read_only=True)

    class Meta:
        model = DocumentCollection
        fields = ('name', 'document_collection_items')
