# Generated by Django 4.2.7 on 2024-06-30 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0007_alter_faculty_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='faculty',
            field=models.ManyToManyField(blank=True, related_name='partners', to='university.faculty', verbose_name='Институты'),
        ),
        migrations.AlterField(
            model_name='studentspeak',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Описание'),
        ),
    ]
