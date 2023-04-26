
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


class AlarmSerializer(serializers.ModelSerializer):
  class Meta:
    model = Alarm
    fields = "__all__"

class AlarmGroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = AlarmGroup()
    fields = "__all__"


  # def create(self, validated_data):

# class AlarmListSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Alarm
#     fields = "__all__"

# class AlarmDetailSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Alarm
#     fields = "__all__"    