from django.shortcuts import render
from rest_framework import status, permissions, generics, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view

from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def alarm_list(request):
  if request.method == 'GET':
    alarm = Alarm.objects.all()
    serializer = AlarmSerializer(alarm, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = AlarmSerialize(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def alarm_detail(request, pk):
  try:
    alarm = Alarm.objects.get(pk=pk)
  except Alarm.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == 'GET':
    serializer = AlarmGroupSerializer(alarm)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = AlarmSerializer(alarm, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'PATCH':
    serializer = AlarmSerializer(alarm, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    alarm.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)










############# ALARM GROUPS #############
class AlarmGroupView(APIView):
  serializer_class = AlarmGroupSerializer

  def get(self, request):
    alarmGroup = [{"name": alarmGroup.aGroupName}
    for alarmGroup in AlarmGroup.objects.all()]
    return Response(alarmGroup)

  def post(self, request):
    serializer = AlarmGroupSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
    return Response(serializer.data)


class AlarmGroupViewSet(viewsets.ModelViewSet):
  queryset = AlarmGroup.objects.all()
  serializer_class = AlarmGroupSerializer


############# ALARMS #############
class AlarmView(APIView):
  serializer_class = AlarmSerializer

  def get(self, request):
    alarm = [{"name": alarm.alarmName, "time": alarm.alarmTime}
    for alarm in Alarm.objects.all()]
    return Response(alarm)

  def post(self, request):
    serializer = AlarmSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
    return Response(serializer.data)


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
