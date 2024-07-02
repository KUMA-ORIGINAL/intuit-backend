# Generated by Django 4.2.7 on 2024-07-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0006_rename_description_trainingprogramitem_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programskills',
            name='program',
            field=models.ManyToManyField(blank=True, related_name='skills', to='university.program', verbose_name='Программа'),
        ),
        migrations.AlterField(
            model_name='programtools',
            name='program',
            field=models.ManyToManyField(blank=True, related_name='tools', to='university.program', verbose_name='Программа'),
        ),
    ]
