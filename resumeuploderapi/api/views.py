from django.shortcuts import render
from api.models import Profile
from rest_framework.response import Response
from api.serializers import ProfileSerailizer
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED
from rest_framework.views import APIView
# Create your views here.

class ProfileView(APIView):

    def post(self,request,format=None):
        serializer=ProfileSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Resume Upload Successfully!','status':'success','candidate':serializer.data},status=HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def get(self,request,format=None):
        candidate=Profile.objects.all()
        serializer=ProfileSerailizer(candidate,many=True)
        return Response({'status':'success','candidate':serializer.data},status=HTTP_200_OK)