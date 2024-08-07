# Generated by Django 4.2.7 on 2024-07-02 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_staff_whatsapp'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True, verbose_name='Номер курса')),
            ],
            options={
                'verbose_name': 'Программа обучения',
                'verbose_name_plural': 'Программы обучения',
            },
        ),
        migrations.AlterModelOptions(
            name='program',
            options={'ordering': ('title',), 'verbose_name': 'Программа', 'verbose_name_plural': 'Программы'},
        ),
        migrations.RenameField(
            model_name='program',
            old_name='description',
            new_name='subtext',
        ),
        migrations.RenameField(
            model_name='program',
            old_name='subtitle',
            new_name='text',
        ),
        migrations.AddField(
            model_name='program',
            name='diploma',
            field=models.CharField(default=1, max_length=255, verbose_name='Диплом'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='program',
            name='employment',
            field=models.CharField(default=1, max_length=255, verbose_name='Трудоустройство'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='program',
            name='study_period',
            field=models.CharField(default=1, max_length=255, verbose_name='Срок обучения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='program',
            name='training_form',
            field=models.CharField(default=1, max_length=255, verbose_name='Форма обучения'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TrainingProgramItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Навык')),
                ('training_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='university.trainingprogram')),
            ],
            options={
                'verbose_name': 'Элемент программы обучения',
                'verbose_name_plural': 'Элементы программы обучения',
            },
        ),
        migrations.AddField(
            model_name='trainingprogram',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training_programs', to='university.program'),
        ),
        migrations.CreateModel(
            name='ProgramTools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255, verbose_name='Инструмент')),
                ('logo', models.ImageField(upload_to='programs/program-tools/', verbose_name='Лого инструмента')),
                ('program', models.ManyToManyField(to='university.program', verbose_name='Программа')),
            ],
            options={
                'verbose_name': 'Инструмент программы',
                'verbose_name_plural': 'Инструменты программы',
            },
        ),
        migrations.CreateModel(
            name='ProgramSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Навык')),
                ('program', models.ManyToManyField(to='university.program', verbose_name='Программа')),
            ],
            options={
                'verbose_name': 'Навык программы',
                'verbose_name_plural': 'Навыки программы',
            },
        ),
    ]
