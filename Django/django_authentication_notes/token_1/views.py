from django.shortcuts import render
from basic_auth.serializers import StudentSerializer
from rest_framework.views import APIView
from basic_auth.models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class StudentModelViewset(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Student.objects.all()

    def get(self,request,format=None):
        print("Request :",request)
        print("User :",request.user)
        print("Auth :",request.auth)
        data=Student.objects.all()
        response=StudentSerializer(data,many=True)
        return Response(response.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

