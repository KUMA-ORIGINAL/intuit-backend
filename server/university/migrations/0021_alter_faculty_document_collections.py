# Generated by Django 4.2.7 on 2025-04-17 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_pages', '0003_alter_documentcollectionitem_document_collection'),
        ('university', '0020_faculty_document_collections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='document_collections',
            field=models.ManyToManyField(blank=True, to='document_pages.documentcollection', verbose_name='Коллекции документов'),
        ),
    ]
