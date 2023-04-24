from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from .models import *
from .serializers import *

# class UserViewSet(viewsets.ModelViewSet):
#     """ API endpoint that allows users to be viewed or edited."""
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]

# class GroupViewSet(viewsets.ModelViewSet):
#     """ API endpoint that allows groups to be viewed or edited. """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.AllowAny] 

class AlarmViewSet(viewsets.ModelViewSet):
  queryset = Alarm.objects.all()
  serializer_class = AlarmSerializer

# class AlarmListViewSet(viewsets.ModelViewSet):
#   queryset = AlarmList.objects.all()
#   serializer_class = AlarmListSerializer

# class AlarmDetailViewSet(viewsets.ModelViewSet):
#   queryset = AlarmDetail.objects.all()
#   serializer_class = AlarmDetailSerializer




  
   















class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
