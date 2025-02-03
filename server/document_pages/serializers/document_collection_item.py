from rest_framework import serializers

from document_pages.models import DocumentCollectionItem


class DocumentCollectionItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentCollectionItem
        fields = ('name', 'document')
