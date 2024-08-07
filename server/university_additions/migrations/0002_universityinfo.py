# Generated by Django 4.2.7 on 2024-07-05 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university_additions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('hours_weekdays', models.CharField(max_length=50, verbose_name='Часы работы в будни')),
                ('hours_saturday', models.CharField(max_length=50, verbose_name='Часы работы в субботу')),
                ('hours_sunday', models.CharField(max_length=50, verbose_name='Часы работы в воскресенье')),
                ('reception_phone', models.CharField(max_length=20, verbose_name='Телефон для общих вопросов')),
                ('admission_office_phone', models.CharField(max_length=20, verbose_name='Телефон приёмной комиссии')),
                ('whatsapp', models.CharField(blank=True, help_text='Введите ссылку на профиль (не обязательное полое)', max_length=100, verbose_name='whatsApp')),
                ('facebook', models.CharField(blank=True, help_text='Введите ссылку на профиль (не обязательное полое)', max_length=100, verbose_name='Facebook')),
                ('telegram', models.CharField(blank=True, help_text='Введите ссылку на профиль (не обязательное полое)', max_length=100, verbose_name='Телеграм')),
                ('instagram', models.CharField(blank=True, help_text='Введите ссылку на профиль (не обязательное полое)', max_length=100, verbose_name='Инстаграм')),
                ('youtube', models.CharField(blank=True, help_text='Введите ссылку на профиль (не обязательное полое)', max_length=100, verbose_name='YouTube')),
            ],
            options={
                'verbose_name': 'Информация об университете',
            },
        ),
    ]
