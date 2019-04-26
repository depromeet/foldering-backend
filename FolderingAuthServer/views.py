from django.shortcuts import render
import os, json


from FolderingAuthServer.models import User

from FolderingAuthServer.serializers import UserModelSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserCreateView(APIView):

    # [POST] /api/signup 인증된 사용자 회원가입 (유저 테이블에 추가)
    def post(self, request, *args, **kwargs):
        received_data = json.dumps(request.data)

        # print(received_data)

        # Model에 저장 위해 직렬화
        serializer = UserModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            result_msg = {'msg' : 'SignUp Success'}

            # 회원 가입 완료
            return Response({'result' : result_msg}, status=status.HTTP_200_OK)

        result_msg = {'msg':'SignUp Failed'}
        return Response({'result' : result_msg }, status=status.HTTP_200_OK)
