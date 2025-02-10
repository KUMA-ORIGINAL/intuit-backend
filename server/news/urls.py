from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, EventViewSet

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet, basename='posts')
router.register(r"events", EventViewSet, basename='events')

urlpatterns = [
    path('', include(router.urls)),
]
