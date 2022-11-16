from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Picture
from .serializers import PictureSerializer
from django.shortcuts import HttpResponseRedirect


class PhotosApiList(APIView):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('login')
        queryset = Picture.objects.filter(author=request.user).order_by('-date')
        serializer = PictureSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PictureSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
