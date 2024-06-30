# Generated by Django 4.2.7 on 2024-06-30 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
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
        migrations.RemoveField(
            model_name='educationlevel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='educationlevel',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='educationlevel',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='educationlevel',
            name='title_2',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='photo',
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='banner',
            field=models.ImageField(default=1, upload_to='education-levels', verbose_name='баннер'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='diploma',
            field=models.CharField(default=1, max_length=255, verbose_name='Диплом'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='employment',
            field=models.CharField(default=1, max_length=255, verbose_name='Трудоустройство'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='program_count',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество программ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='study_period',
            field=models.CharField(default=1, max_length=255, verbose_name='Срок обучения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='subtext',
            field=models.CharField(default=1, max_length=255, verbose_name='Подтекст'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='text',
            field=models.CharField(default=1, max_length=255, verbose_name='Главный текст'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faculty',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Баннер'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='description',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='education_level',
        ),
        migrations.CreateModel(
            name='StudentReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='ФИО')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='students/reviews', verbose_name='Фото')),
                ('video', models.FileField(upload_to='students/reviews-video', verbose_name='Видео')),
                ('video_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на видео')),
                ('education_level', models.ManyToManyField(blank=True, to='university.educationlevel', verbose_name='Уровни образования')),
                ('faculty', models.ManyToManyField(blank=True, null=True, related_name='student_reviews', to='university.faculty', verbose_name='Институты')),
            ],
            options={
                'verbose_name': 'Отзыв студента',
                'verbose_name_plural': 'Отзывы студентов',
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
        migrations.AddField(
            model_name='faculty',
            name='education_level',
            field=models.ManyToManyField(to='university.educationlevel', verbose_name='Уровень образования'),
        ),
    ]