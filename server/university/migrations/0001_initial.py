# Generated by Django 4.2.7 on 2024-06-30 10:26

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('subtitle', models.CharField(blank=True, max_length=250, verbose_name='Подзаголовок')),
            ],
            options={
                'verbose_name': 'Деталь',
                'verbose_name_plural': 'Детали',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='EducationLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(verbose_name='ссылка')),
                ('subtitle', models.CharField(blank=True, max_length=255, verbose_name='Под название')),
                ('banner', models.ImageField(upload_to='education-levels', verbose_name='баннер')),
                ('text', models.TextField(verbose_name='Главный текст')),
                ('subtext', models.TextField(verbose_name='Под текст')),
                ('program_count', models.PositiveIntegerField(blank=True, default=0, verbose_name='Количество программ')),
                ('study_period', models.CharField(max_length=255, verbose_name='Срок обучения')),
                ('employment', models.CharField(max_length=255, verbose_name='Трудоустройство')),
                ('diploma', models.CharField(max_length=255, verbose_name='Диплом')),
            ],
            options={
                'verbose_name': 'Уровень образования',
                'verbose_name_plural': 'Уровни образования',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(verbose_name='ссылка')),
                ('banner', models.ImageField(upload_to='', verbose_name='Баннер')),
                ('subtitle', models.CharField(blank=True, max_length=250, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Главный текст')),
                ('subtext', models.TextField(verbose_name='Под текст')),
                ('education_level', models.ManyToManyField(to='university.educationlevel', verbose_name='Уровень образования')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультеты',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Должность')),
                ('level', models.IntegerField(verbose_name='Приоритет должности')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
                'ordering': ['level'],
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='ФИО')),
                ('slug', models.SlugField(blank=True, verbose_name='Ссылка')),
                ('rank', models.CharField(choices=[('no', 'Отсутствует'), ('professor', 'Почетный профессор'), ('doctor', 'Почетный доктор')], default='no', max_length=50, verbose_name='Статус')),
                ('status', models.CharField(choices=[('1', 'Преподаватель'), ('2', 'Старший преподаватель'), ('3', 'Кандитат наук'), ('4', 'Профессор'), ('5', 'Доцент')], default='1', max_length=20, verbose_name='Звание')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.FileField(upload_to='faculty/images/teachers', verbose_name='Изображение')),
                ('facebook', models.CharField(blank=True, help_text='Введите ссылку на профиль (не обязательное полое)', max_length=100, verbose_name='facebook')),
                ('telegram', models.CharField(blank=True, help_text='Введите ссылку на профиль (не обязательное полое)', max_length=100, verbose_name='Телеграм')),
                ('instagram', models.CharField(blank=True, help_text='Введите ссылку на профиль (не обязательное полое)', max_length=100, verbose_name='Инстаграм')),
                ('youtube', models.CharField(blank=True, help_text='Введите ссылку на профиль (не обязательное полое)', max_length=100, verbose_name='YouTube')),
                ('curriculum_vitae', models.FileField(blank=True, upload_to='faculty/files/cv', verbose_name='Сurriculum Vitae')),
                ('cv', models.TextField(blank=True, null=True)),
                ('faculty', models.ManyToManyField(blank=True, null=True, related_name='teachers', to='university.faculty', verbose_name='Факультеты')),
                ('position', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='university.position', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('slug', models.SlugField(verbose_name='ссылка')),
                ('subtitle', models.CharField(blank=True, max_length=250, verbose_name='Заголовок')),
                ('description', ckeditor.fields.RichTextField(default='Описание', verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='programs', verbose_name='Фото')),
                ('education_level', models.ManyToManyField(to='university.educationlevel', verbose_name='Уровень образования')),
                ('faculty', models.ManyToManyField(to='university.faculty', verbose_name='Факультет')),
            ],
            options={
                'verbose_name': 'Программа обучения',
                'verbose_name_plural': 'Программы обучения',
                'ordering': ('title',),
            },
        ),
    ]
