from django.shortcuts import render


# Create your views here.
from  rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from remainder_api.serializers import UserSerializer


class UserCreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
