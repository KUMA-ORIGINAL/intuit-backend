# Generated by Django 4.2.7 on 2024-12-24 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university_additions', '0008_pageitem_description_en_pageitem_description_ky_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pageitem',
            name='category',
        ),
        migrations.AddField(
            model_name='pageitem',
            name='slug',
            field=models.SlugField(default=1, verbose_name='ссылка'),
            preserve_default=False,
        ),
    ]
