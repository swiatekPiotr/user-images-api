from django.urls import path, include
from .views import PhotoListCreateAPIView, PhotoRetrieveUpdateAPIView


urlpatterns = [
    path('pictures/', include('django.contrib.auth.urls')),
    path('pictures/', PhotoListCreateAPIView.as_view(), name='photo-api-list'),
    path('pictures/<int:pk>', PhotoRetrieveUpdateAPIView.as_view(), name='photo-api-retrieve'),
]
