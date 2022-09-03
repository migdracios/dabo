from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


# 회원기능 관련 API
class SignView(APIView):
    # 회원가입
    def post(self, request):
        return Response({})

    # 회원수정
    def put(self, request):
        return Response({})

    # 회원탈퇴, 비활성화
    def delete(self, request):
        return Response({})
