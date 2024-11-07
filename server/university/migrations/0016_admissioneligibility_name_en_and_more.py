# Generated by Django 4.2.7 on 2024-11-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0015_alter_faculty_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissioneligibility',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='admissioneligibility',
            name='name_ky',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='admissioneligibility',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='detail',
            name='subtitle_en',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AddField(
            model_name='detail',
            name='subtitle_ky',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AddField(
            model_name='detail',
            name='subtitle_ru',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AddField(
            model_name='detail',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='detail',
            name='title_ky',
            field=models.CharField(max_length=500, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='detail',
            name='title_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='diploma_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Диплом'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='diploma_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Диплом'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='diploma_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Диплом'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='employment_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Трудоустройство'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='employment_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Трудоустройство'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='employment_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Трудоустройство'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='study_period_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Срок обучения'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='study_period_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Срок обучения'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='study_period_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Срок обучения'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='subtext_en',
            field=models.TextField(null=True, verbose_name='Под текст'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='subtext_ky',
            field=models.TextField(null=True, verbose_name='Под текст'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='subtext_ru',
            field=models.TextField(null=True, verbose_name='Под текст'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='subtitle_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Под название'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='subtitle_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Под название'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='subtitle_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Под название'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Главный текст'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='text_ky',
            field=models.TextField(null=True, verbose_name='Главный текст'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Главный текст'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='subtext_en',
            field=models.TextField(null=True, verbose_name='Под текст'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='subtext_ky',
            field=models.TextField(null=True, verbose_name='Под текст'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='subtext_ru',
            field=models.TextField(null=True, verbose_name='Под текст'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='subtitle_en',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='subtitle_ky',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='subtitle_ru',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Главный текст'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='text_ky',
            field=models.TextField(null=True, verbose_name='Главный текст'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Главный текст'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='position',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='position',
            name='title_ky',
            field=models.CharField(max_length=100, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='position',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='program',
            name='diploma_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Диплом'),
        ),
        migrations.AddField(
            model_name='program',
            name='diploma_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Диплом'),
        ),
        migrations.AddField(
            model_name='program',
            name='diploma_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Диплом'),
        ),
        migrations.AddField(
            model_name='program',
            name='employment_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Трудоустройство'),
        ),
        migrations.AddField(
            model_name='program',
            name='employment_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Трудоустройство'),
        ),
        migrations.AddField(
            model_name='program',
            name='employment_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Трудоустройство'),
        ),
        migrations.AddField(
            model_name='program',
            name='study_period_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Срок обучения'),
        ),
        migrations.AddField(
            model_name='program',
            name='study_period_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Срок обучения'),
        ),
        migrations.AddField(
            model_name='program',
            name='study_period_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Срок обучения'),
        ),
        migrations.AddField(
            model_name='program',
            name='subtext_en',
            field=models.TextField(default='Описание', null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='program',
            name='subtext_ky',
            field=models.TextField(default='Описание', null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='program',
            name='subtext_ru',
            field=models.TextField(default='Описание', null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='program',
            name='text_en',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='program',
            name='text_ky',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='program',
            name='text_ru',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='program',
            name='title_en',
            field=models.CharField(max_length=250, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='program',
            name='title_ky',
            field=models.CharField(max_length=250, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='program',
            name='title_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='program',
            name='training_form_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Форма обучения'),
        ),
        migrations.AddField(
            model_name='program',
            name='training_form_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Форма обучения'),
        ),
        migrations.AddField(
            model_name='program',
            name='training_form_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Форма обучения'),
        ),
        migrations.AddField(
            model_name='programprofessions',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание профессии'),
        ),
        migrations.AddField(
            model_name='programprofessions',
            name='description_ky',
            field=models.TextField(null=True, verbose_name='Описание профессии'),
        ),
        migrations.AddField(
            model_name='programprofessions',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание профессии'),
        ),
        migrations.AddField(
            model_name='programprofessions',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Профессия'),
        ),
        migrations.AddField(
            model_name='programprofessions',
            name='name_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Профессия'),
        ),
        migrations.AddField(
            model_name='programprofessions',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Профессия'),
        ),
        migrations.AddField(
            model_name='programskills',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Навык'),
        ),
        migrations.AddField(
            model_name='programskills',
            name='name_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Навык'),
        ),
        migrations.AddField(
            model_name='programskills',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Навык'),
        ),
        migrations.AddField(
            model_name='programtools',
            name='description_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание инструмента'),
        ),
        migrations.AddField(
            model_name='programtools',
            name='description_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание инструмента'),
        ),
        migrations.AddField(
            model_name='programtools',
            name='description_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание инструмента'),
        ),
        migrations.AddField(
            model_name='programtools',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Инструмент'),
        ),
        migrations.AddField(
            model_name='programtools',
            name='name_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Инструмент'),
        ),
        migrations.AddField(
            model_name='programtools',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Инструмент'),
        ),
        migrations.AddField(
            model_name='staff',
            name='cv_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='cv_ky',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='cv_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='staff',
            name='description_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='staff',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='staff',
            name='name_en',
            field=models.CharField(max_length=250, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='staff',
            name='name_ky',
            field=models.CharField(max_length=250, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='staff',
            name='name_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='staff',
            name='rank_en',
            field=models.CharField(choices=[('no', 'Отсутствует'), ('professor', 'Почетный профессор'), ('doctor', 'Почетный доктор')], default='no', max_length=50, null=True, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='staff',
            name='rank_ky',
            field=models.CharField(choices=[('no', 'Отсутствует'), ('professor', 'Почетный профессор'), ('doctor', 'Почетный доктор')], default='no', max_length=50, null=True, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='staff',
            name='rank_ru',
            field=models.CharField(choices=[('no', 'Отсутствует'), ('professor', 'Почетный профессор'), ('doctor', 'Почетный доктор')], default='no', max_length=50, null=True, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='staff',
            name='status_en',
            field=models.CharField(choices=[('1', 'Преподаватель'), ('2', 'Старший преподаватель'), ('3', 'Кандитат наук'), ('4', 'Профессор'), ('5', 'Доцент')], default='1', max_length=20, null=True, verbose_name='Звание'),
        ),
        migrations.AddField(
            model_name='staff',
            name='status_ky',
            field=models.CharField(choices=[('1', 'Преподаватель'), ('2', 'Старший преподаватель'), ('3', 'Кандитат наук'), ('4', 'Профессор'), ('5', 'Доцент')], default='1', max_length=20, null=True, verbose_name='Звание'),
        ),
        migrations.AddField(
            model_name='staff',
            name='status_ru',
            field=models.CharField(choices=[('1', 'Преподаватель'), ('2', 'Старший преподаватель'), ('3', 'Кандитат наук'), ('4', 'Профессор'), ('5', 'Доцент')], default='1', max_length=20, null=True, verbose_name='Звание'),
        ),
        migrations.AddField(
            model_name='trainingprogramitem',
            name='name_en',
            field=models.TextField(null=True, verbose_name='Навык'),
        ),
        migrations.AddField(
            model_name='trainingprogramitem',
            name='name_ky',
            field=models.TextField(null=True, verbose_name='Навык'),
        ),
        migrations.AddField(
            model_name='trainingprogramitem',
            name='name_ru',
            field=models.TextField(null=True, verbose_name='Навык'),
        ),
    ]
