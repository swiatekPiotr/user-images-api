from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Picture
from .serializers import PictureSerializer


class PhotoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Picture.objects.all().order_by('-date')
    serializer_class = PictureSerializer

    def post(self, request, *args, **kwargs):
        serializer = PictureSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhotoRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Picture.objects.all().order_by('-date')
    serializer_class = PictureSerializer
    lookup_field = 'pk'
