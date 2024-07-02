# Generated by Django 4.2.7 on 2024-07-02 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionEligibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Допуск к поступлению',
                'verbose_name_plural': 'Допуск к поступлениям',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='admission_eligibility',
            field=models.ManyToManyField(to='university.admissioneligibility', verbose_name='Подходимость для поступления'),
        ),
    ]
