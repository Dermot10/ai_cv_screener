from django.urls import path, include
from .views import CvUploadView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CvUploadView, basename='cv-upload')


urlpatterns = [
    path('upload/', include(router.urls)),
    
]
