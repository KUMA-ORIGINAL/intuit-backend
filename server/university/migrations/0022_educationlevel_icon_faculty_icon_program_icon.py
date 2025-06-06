# Generated by Django 4.2.7 on 2025-04-21 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0021_alter_faculty_document_collections'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationlevel',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='education-levels-icons', verbose_name='Иконка'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='faculties-icons', verbose_name='Иконка'),
        ),
        migrations.AddField(
            model_name='program',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='programs-icons', verbose_name='Иконка'),
        ),
    ]
