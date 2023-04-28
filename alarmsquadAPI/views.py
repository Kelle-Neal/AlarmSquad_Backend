from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status, permissions, generics, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

import json 

from .models import *
from .serializers import *

############# ALARMS #############
class AlarmViewSet(viewsets.ModelViewSet):
    queryset = Alarm.objects.all()
    serializer_class = AlarmSerializer

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().partial_update(request, *args, **kwargs)

    def edit_alarm(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



# @csrf_exempt
# def alarms(request):
#     if request.method == 'GET':
#         alarms = Alarm.objects.all()
#         return JsonResponse({'alarms': list(alarms.values())})

#     elif request.method == 'POST':
#         data = json.loads(request.body)
#         alarm = Alarm()
#         alarm.alarmGroup = data['alarmGroup']
#         alarm.alarmDate = data['alarmDate']
#         alarm.alarmTime = data['alarmTime']
#         alarm.alarmVolume = data['alarmVolume']
#         alarm.ringtone = data['ringtone']
#         alarm.save()
#         return JsonResponse({'alarm': model_to_dict(alarm)})

# @csrf_exempt
# def edit_alarm(request, pk):
#     alarm = get_object_or_404(Alarm, pk=pk)

#     if request.method == 'POST':
#         data = json.loads(request.body)
#         alarm.alarmGroup = data['alarmGroup']
#         alarm.alarmDate = data['alarmDate']
#         alarm.alarmTime = data['alarmTime']
#         alarm.alarmVolume = data['alarmVolume']
#         alarm.ringtone = data['ringtone']
#         alarm.save()
#         return JsonResponse({'alarm': model_to_dict(alarm)})

#     return render(request, 'edit_alarm.html', {'alarm': alarm})        

# @csrf_exempt
# def delete_alarm(request, alarm_id):
#   alarm = get_object_or_404(Alarm, id=alarm_id)
#   if request.method == 'DELETE':
#     alarm.delete()
#     return JsonResponse({'message': 'Alarm deleted successfully'})


############# RINGTONES #############
class RingtoneViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ringtone.objects.all()
    serializer_class = RingtoneSerializer


############# ALARM GROUPS #############
class AlarmGroupViewSet(viewsets.ModelViewSet):
    queryset = AlarmGroup.objects.all()
    serializer_class = AlarmGroupSerializer






# ############# RINGTONES #############
# class RingtoneViewSet(viewsets.ReadOnlyModelViewSet):
#   queryset = Ringtone.objects.all()
#   serializer_class = RingtoneSerializer


# ############# ALARM GROUPS #############
# class AlarmGroupView(APIView):
#   serializer_class = AlarmGroupSerializer
#   def get(self, request):
#     alarmGroups = AlarmGroup.objects.all()
#     serializer = AlarmGroupSerializer(alarmGroups, many=True)
#     return Response(serializer.data)

#   def post(self, request):
#     serializer = AlarmGroupSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#     return Response(serializer.data)


# class AlarmGroupViewSet(viewsets.ModelViewSet):
#   queryset = AlarmGroup.objects.all()
#   serializer_class = AlarmGroupSerializer


# ############# ALARMS #############
# class AlarmView(APIView):
#   serializer_class = AlarmSerializer

#   def get(self, request):
#     alarms = Alarm.objects.all()
#     serializer = AlarmSerializer(alarms, many=True)
#     return Response(serializer.data)

#   def post(self, request):
#     serializer = AlarmSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class AlarmViewSet(viewsets.ModelViewSet):
#     queryset = Alarm.objects.all()
#     serializer_class = AlarmSerializer



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


############# TIMER GROUPS #############
class TimerGroupView(APIView):
  serializer_class = TimerGroupSerializer

  def get(self, request):
    timerGroup = [{"name": timerGroup.tGroupName}
    for timerGroup in TimerGroup.objects.all()]
    return Response(timerGroup)

  def post(self, request):
    serializer = TimerGroupSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
    return Response(serializer.data)


class TimerGroupViewSet(viewsets.ModelViewSet):
  queryset = TimerGroup.objects.all()
  serializer_class = TimerGroupSerializer



############# TIMERS #############
class TimerView(APIView):
  serializer_class = TimerSerializer

  def get(self, request):
    timer = [{"name": timer.timerName, "time": timer.timerTime}
    for Timer in Timer.objects.all()]
    return Response(timer)

  def post(self, request):
    serializer = TimerSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
    return Response(serializer.data)


class TimerViewSet(viewsets.ModelViewSet):
  queryset = Timer.objects.all()
  serializer_class = TimerSerializer


# @api_view(['GET', 'POST'])
# def alarm_list(request):
#   if request.method == 'GET':
#     alarm = Alarm.objects.all()
#     serializer = AlarmSerializer(alarm, many=True)
#     return Response(serializer.data)

#   elif request.method == 'POST':
#     serializer = AlarmSerialize(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def alarm_detail(request, pk):
#   try:
#     alarm = Alarm.objects.get(pk=pk)
#   except Alarm.DoesNotExist:
#     return Response(status=status.HTTP_404_NOT_FOUND)
#   if request.method == 'GET':
#     serializer = AlarmGroupSerializer(alarm)
#     return Response(serializer.data)
#   elif request.method == 'PUT':
#     serializer = AlarmSerializer(alarm, data=request.data)

#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#   elif request.method == 'PATCH':
#     serializer = AlarmSerializer(alarm, data=request.data, partial=True)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#   elif request.method == 'DELETE':
#     alarm.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)  