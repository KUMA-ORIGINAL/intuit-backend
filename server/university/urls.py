from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"education-levels",
                views.EducationLevelViewSet,
                basename='education-levels')
router.register(r"faculties",
                views.FacultyViewSet,
                basename='faculties')
router.register(r"programs",
                views.ProgramViewSet,
                basename='programs')
router.register(r"staffs",
                views.StaffViewSet,
                basename='staffs')
router.register(r'positions',
                views.PositionViewSet,
                basename="positions")

urlpatterns = [
    path('', include(router.urls)),
]

