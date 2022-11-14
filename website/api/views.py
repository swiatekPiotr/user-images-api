from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Picture
from .serializers import PictureSerializer


class PhotosApiList(APIView):
    def get(self, request):
        queryset = Picture.objects.filter(author=request.user).order_by('-date')
        serializer = PictureSerializer(queryset, many=True)
        return Response(serializer.data)
