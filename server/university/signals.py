from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from university.models import Program, EducationLevel, Faculty


@receiver(m2m_changed, sender=Program.education_level.through)
def update_program_count(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        for education_level_id in pk_set:
            education_level = EducationLevel.objects.get(pk=education_level_id)
            education_level.program_count = Program.objects.filter(education_level=education_level).count()
            education_level.save()


@receiver(m2m_changed, sender=Faculty.education_level.through)
def update_faculty_count(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        for education_level_id in pk_set:
            education_level = EducationLevel.objects.get(pk=education_level_id)
            education_level.faculty_count = Faculty.objects.filter(education_level=education_level).count()
            education_level.save()
