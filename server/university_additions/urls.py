from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"partners",
                views.PartnerViewSet,
                basename='partners')
router.register(r"student-reviews",
                views.StudentReviewViewSet,
                basename='student-reviews')
router.register(r"student-speakers",
                views.StudentSpeakViewSet,
                basename='student-speakers')
router.register(r'university-info',
                views.UniversityInfoViewSet,
                basename='university-info')

urlpatterns = [
    path('', include(router.urls)),
]
