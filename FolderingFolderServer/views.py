from rest_framework import viewsets 
from .models import Link, Text, Image, Folder
from .serializers import LinkSerializer, TextSerializer, ImageSerializer, FolderSerializer
from rest_framework.response import Response
from rest_framework.decorators import detail_route


class FolderViewSet(viewsets.ModelViewSet): 
   queryset = Folder.objects.all() 
   serializer_class = FolderSerializer

   @detail_route(methods=['post'], url_path='createfolder')
   def createfolder(self, request, pk=None):
      folder = Folder.objects.create(pk=pk)
      return Response("success")

   @detail_route(methods=['get'], url_path='showfolder')
   def showfolder(self, request, pk=None):
      folder = Folder.objects.all(pk=pk)
      return Response(folder)

   @detail_route(methods=['delete'], url_path='deletefolder')
   def deletefolder(self, request, pk=None):
      folder = Folder.objects.all(pk=pk)
      folder.delete()
      return Response("success")   

class LinkViewSet(viewsets.ModelViewSet): 
   queryset = Link.objects.all() 
   serializer_class = LinkSerializer 

class TextViewSet(viewsets.ModelViewSet): 
   queryset = Text.objects.all() 
   serializer_class = TextSerializer 

class ImageViewSet(viewsets.ModelViewSet): 
   queryset = Image.objects.all() 
   serializer_class = ImageSerializer 