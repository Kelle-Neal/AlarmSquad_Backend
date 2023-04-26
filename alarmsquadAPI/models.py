from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
  #birthday = models.DateField(null = True)
  pass
  
  def __str__(self):
    return self.username

############# ALARMS #############
class Alarm(models.Model):
  alarmName = models.CharField(max_length=300)
  alarmTime = models.TimeField()
  alarmRepeat = models.BooleanField(default=False, blank=True, null=True)
  alarmDate = models.DateField(blank=True, null=True)
  alarmDays = models.DateField(blank=True, null=True)
  alarmSnooze = models.BooleanField(default=False, blank=True, null=True)
  # alarmVibrate = models.BooleanField(default=True)
  alarmSilent = models.BooleanField(default=False, blank=True, null=True)
  alarmRingtone = models.IntegerField(blank=True, null=True)
  alarmVolume = models.IntegerField(blank=True, null=True)
  # alarmIncreaseVolume = models.BooleanField(default=False, blank=True, null=True)
  alarmInGroup = models.BooleanField(default=False, blank=True, null=True)
  alarmGroup = models.IntegerField(blank=True, null=True)
  alarmIsEnabled = models.BooleanField(default=True)

  def __str__(self):
    return f'{self.alarmName}'

############# ALARM GROUPS #############
class AlarmGroup(models.Model):
  aGroupName = models.CharField(max_length=300)
  aGroupRepeat = models.BooleanField(default=False, blank=True, null=True)
  aGroupDate = models.DateField(blank=True, null=True)
  aGroupDays = models.DateField(blank=True, null=True)
   # aGroupVibrate = models.BooleanField(default=True)
  aGroupSilent = models.BooleanField(default=False, blank=True, null=True)
  aGroupRingtone = models.IntegerField(blank=True, null=True)
  aGroupVolume = models.IntegerField(blank=True, null=True)
  # aGroupIncreaseVolume = models.BooleanField(default=False, blank=True, null=True)
  aGroupIsEnabled = models.BooleanField(default=True)

  def __str__(self):
    return f'{self.aGroupName}'

############# ALARM BRIDGE #############
class AlarmToGroupBridge(models.Model):
  alarmId = models.IntegerField()
  alarmGroupId = models.IntegerField()



# class auth_user(AbstractUser):
#   username = models.CharField()
#   password = models.CharField()
#   firstName = models.CharField()
#   lastName = models.CharField()
#   email = models.EmailField()
#   isActive = models.BooleanField(default=True)
#   dateJoined = models.DateTimeField()

#   def __str__(self):
#     return f'{self.name}'
      

  # class Timer(models.Model): 
  #   timerName = models.CharField()
  #   timerLength = models.TimeField()
  #   # timerVibrate = models.BooleanField(default=True)
  #   timerSilent = models.BooleanField(default=False)
  #   timerRingtone = models.IntegerField()
  #   timerVolume = models.IntegerField()
  #   # timerIncreaseVolume = models.BooleanField(default=False)
  #   timerInGroup = models.BooleanField(default=False)
  #   timerGroup = models.IntegerField()
  #   timerIsEnabled = models.BooleanField(default=True)

  #   def __str__(self):
  #     return f'{self.timerName}'

  # class TimerGroup(models.Model):
  #   tGroupName = models.CharField()
  #   # tGroupVibrate = models.BooleanField(default=True)
  #   tGroupSilent = models.BooleanField(default=False)
  #   tGroupRingtone = models.IntegerField()
  #   tGroupVolume = models.IntegerField()
  #   # tGroupIncreaseVolume = models.BooleanField(default=False)    
  #   tGroupIsEnabled = models.BooleanField(default=True)

  # def __str__(self):
  #   return f'{self.tGroupName}'

  # class TimerToGroupBridge(models.Model):
  #   timerId = models.IntegerField()
  #   timerGroupId = models.IntegerField()

  # def __str__(self):
  #   return f'{self.name}'


  # class ringtones(models.Model):
  #   name = models.CharField()

  # def __str__(self):
  #   return f'{self.name}'


  # class AlertTypes(models.Model):
  #   alarmAlert = models.IntegerField()
  #   alarmGroupAlert = models.IntegerField()
  #   timerAlert = models.IntegerField()
  #   timerGroupAlert = models.IntegerField()

  # def __str__(self):
  #   return f'{self.name}'


  # class TypeOfAlert(models.Model):
  #   name = models.CharField()

  # def __str__(self):
  #   return f'{self.name}'  


  # class Notifications(models.Model):
  #   alert = models.IntegerField()
  #   alertType = models.IntegerField()
  #   user = models.IntegerField()

  # def __str__(self):
  #   return f'{self.name}'  
  

  
  