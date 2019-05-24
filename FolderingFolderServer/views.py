from rest_framework import viewsets 
from .models import Link, Text, Image, Folder, User
from .serializers import LinkSerializer, TextSerializer, ImageSerializer, FolderSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import permissions
from .permission import IsAuthorOrCantDelete
from rest_framework import status
from django.http import Http404

class FolderViewSet(viewsets.ModelViewSet): 
   queryset = Folder.objects.all() 
   serializer_class = FolderSerializer

   # To do : 토큰 인증받아서 작성자만 삭제할 수 있게 해줘
      
   # def destroy(self, request, *args, **kwargs):
   #      try:
   #         instance = self.get_object()
   #         self.perform_destroy(instance)
   #      except Http404:
   #         pass
   #      return Response(status=status.HTTP_204_NO_CONTENT)




class LinkViewSet(viewsets.ModelViewSet): 
   queryset = Link.objects.all() 
   serializer_class = LinkSerializer 

class TextViewSet(viewsets.ModelViewSet): 
   queryset = Text.objects.all() 
   serializer_class = TextSerializer 

class ImageViewSet(viewsets.ModelViewSet): 
   queryset = Image.objects.all() 
   serializer_class = ImageSerializer 

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer