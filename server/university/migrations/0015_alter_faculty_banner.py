# Generated by Django 4.2.7 on 2024-11-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0014_faculty_program_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='banner',
            field=models.FileField(upload_to='faculties', verbose_name='Баннер'),
        ),
    ]
