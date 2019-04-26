from django.shortcuts import render
import os, json


from FolderingAuthServer.models import User

from FolderingFolderServer.models import (
            Folder,
            Participation,
            Inclusion,
            Link,
            Image,
            Text
            )

from FolderingAuthServer.serializers import UserModelSerializer

from FolderingFolderServer.serializers import(
            FolderModelSerializer,
            ParticipationModelSerializer,
            InclusionModelSerializer,
            LinkModelSerializer,
            ImageModelSerializer,
            TextModelSerializer,
            FolderListSerializer
            )

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# 사용자가 가지고 있는 폴더 리스트 보기
class FolderListView(APIView):
    serializer_class = FolderModelSerializer

    # [GET] /api/folder/{userId} 사용자의 폴더 리스트 확인
    def get(self, *args, **kwargs):
        try:
            participation_queryset = self.get_participation_queryset() # 참여 전체 목록을 가져옴
            folder_queryset = self.get_folder_queryset() # 폴더 전체 목록을 가져옴
            # user_queryset = self.get_user_queryset() # 사용자 전체 목록을 가져옴
        except:
            return Response(status=status.HTTP_200_OK)

        user_uid = int(self.kwargs['userId'])  # url에 있는 사용자 userId를 가져옴
        # print("[USER_UID] "+str(user_uid))

        if user_uid is not None:
            user_query_object = User.objects.get(user_uid=user_uid)
            user_pk = user_query_object.pk
            # print("[USER_PK] "+str(user_query_object.pk))
            participation_queryset = participation_queryset.filter(user_uid_id=user_pk) # 요청한 사용자의 pk로 사용자가 참여한 row 만 가져온다
            folder_queryset = folder_queryset.filter(pk__in=participation_queryset.values('folder_uid')) # 참여 정보에서의 folder id로 folder 가져옴

            serializer = FolderListSerializer(folder_queryset, many=True) # 폴더 이름 가져오기 위함

            # print(serializer.data)

            folder_list = {"folder_list" : serializer.data} # 사용자가 참여한 폴더 리스트 제공

            return Response({"result" : folder_list},status=status.HTTP_200_OK)


        return Response(status=status.HTTP_200_OK) # TODO 400, 500 error 추가 필요


    def get_participation_queryset(self, *args, **kwargs):
        participation_queryset = Participation.objects.all() # 참여 목록을 가져옴
        return participation_queryset

    def get_folder_queryset(self, *args, **kwargs):
        folder_queryset = Folder.objects.all() # 폴더 목록을 가져옴
        return folder_queryset

    def get_user_queryset(self, *args, **kwargs):
        user_queryset = User.objects.all() # 사용자 목록을 가져옴
        return user_queryset

# 새로운 폴더 생성
class FolderCreateView(APIView):

    # [POST] /api/folder/{userId} 사용자의 폴더 리스트 확인
    def post(self, request, *args, **kwargs):
        received_data = json.dumps(request.data)

        # print(received_data)

        try:
            user_obj = self.get_user_obj(int(self.kwargs['userId'])) # userId를 사용하는 user object
            user_pk = user_obj.pk

            received_data = {"folder_name": request.data['folder_name'], "manager_id" : user_pk}

            received_data = json.dumps(received_data)
            print("[RECEIVED_DATA] "+received_data)

            received_data = json.loads(received_data)
        except:
            return Response({'result': {'msg': 'Folder Create Failed'}},status=status.HTTP_200_OK)


        # Model에 저장 위해 직렬화
        serializer = FolderModelSerializer(data=received_data)

        if serializer.is_valid():
            serializer.save()

            result_msg = "폴더 "+ str(received_data['folder_name']) +"이(가) 생성되었습니다."

            # 폴더 생성 완료
            return Response({'result': {"data": serializer.data,"msg":result_msg}}, status=status.HTTP_200_OK)

        result_msg = {'msg': 'Folder Create Failed'}
        return Response({'result': result_msg}, status=status.HTTP_200_OK)


    def get_user_obj(self, user_uid ,*args, **kwargs):
        user_obj = User.objects.get(user_uid=user_uid) # 사용자 목록을 가져옴
        return user_obj




# from rest_framework import viewsets
# from .models import Link, Text, Image, Folder
# from .serializers import LinkSerializer, TextSerializer, ImageSerializer, FolderSerializer
# from rest_framework.response import Response
# from rest_framework.decorators import detail_route
#
#
# class FolderViewSet(viewsets.ModelViewSet):
#    queryset = Folder.objects.all()
#    serializer_class = FolderSerializer
#
#    @detail_route(methods=['post'], url_path='createfolder')
#    def createfolder(self, request, pk=None):
#       folder = Folder.objects.create(pk=pk)
#       return Response("success")
#
#    @detail_route(methods=['get'], url_path='showfolder')
#    def showfolder(self, request, pk=None):
#       folder = Folder.objects.all(pk=pk)
#       return Response(folder)
#
#    @detail_route(methods=['delete'], url_path='deletefolder')
#    def deletefolder(self, request, pk=None):
#       folder = Folder.objects.all(pk=pk)
#       folder.delete()
#       return Response("success")
#
# class LinkViewSet(viewsets.ModelViewSet):
#    queryset = Link.objects.all()
#    serializer_class = LinkSerializer
#
# class TextViewSet(viewsets.ModelViewSet):
#    queryset = Text.objects.all()
#    serializer_class = TextSerializer
#
# class ImageViewSet(viewsets.ModelViewSet):
#    queryset = Image.objects.all()
#    serializer_class = ImageSerializer