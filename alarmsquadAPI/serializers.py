from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True
  )
  username = serializers.CharField()
  password = serializers.CharField(min_length=8, write_only=True)
  
  class Meta:
    model = CustomUser
    fields = ('email', 'username', 'password', 'first_name', 'last_name')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    password = validated_data.pop('password', None)
    instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
    if password is not None:
        instance.set_password(password)
    instance.save()
    return instance

############# RINGTONES #############
class RingtoneSerializer(serializers.ModelSerializer):
  soundFile = serializers.FileField(required=True)

  class Meta:
    model = Ringtone
    fields = "__all__"

############# ALARM GROUPS #############
class AlarmGroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = AlarmGroup
    fields = "__all__"

############# ALARMS #############
class AlarmSerializer(serializers.ModelSerializer):
    # ringtone = RingtoneSerializer(required=False)
    alarmGroup = serializers.PrimaryKeyRelatedField(queryset=AlarmGroup.objects.all(), required=False)
    class Meta:
        model = Alarm
        fields = "__all__"

############# TIMER GROUPS #############
class TimerGroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = TimerGroup
    fields = "__all__"

############# TIMERS #############
class TimerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Timer
    fields = "__all__"
