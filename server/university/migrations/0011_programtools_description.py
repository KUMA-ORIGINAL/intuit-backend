# Generated by Django 4.2.7 on 2024-07-05 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0010_alter_program_subtext_alter_program_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='programtools',
            name='description',
            field=models.CharField(default=1, max_length=255, verbose_name='Описание инструмента'),
            preserve_default=False,
        ),
    ]
