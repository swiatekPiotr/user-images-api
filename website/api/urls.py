from django.urls import path
from .views import PhotosApiList


urlpatterns = [
    path('', PhotosApiList.as_view(), name='expense-api-list'),
]
