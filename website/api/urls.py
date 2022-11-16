from django.urls import path, include
from .views import PhotosApiList


urlpatterns = [
    path('pictures/', include('django.contrib.auth.urls')),
    path('pictures/', PhotosApiList.as_view(), name='expense-api-list'),
]
