# Generated by Django 4.2.7 on 2024-07-05 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0009_alter_program_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='subtext',
            field=models.TextField(default='Описание', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='program',
            name='text',
            field=models.TextField(blank=True, max_length=250, verbose_name='Заголовок'),
        ),
    ]
