from django.urls import path, include
from rest_framework import routers

from document_pages.views import DocumentPageViewSet

router = routers.DefaultRouter()
router.register(r'', DocumentPageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
