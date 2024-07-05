from django.contrib import admin

from university_additions.models.university_info import UniversityInfo


@admin.register(UniversityInfo)
class UniversityInfoAdmin(admin.ModelAdmin):
    list_display = ['address']
    def has_add_permission(self, request):
        if UniversityInfo.objects.exists():
            return False
        return super().has_add_permission(request)
