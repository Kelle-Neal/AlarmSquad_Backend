from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # birthday = models.DateField(null = True)
    pass

    def __str__(self):
        return self.username

############# RINGTONES #############
class Ringtone(models.Model):
    name = models.JSONField()
    soundFile = models.FileField(upload_to='ringtones/')

    def __str__(self):
        if self.name.get('name'):
            return self.name.get('name')
        else:
            return 'Ringtone'

############# ALARM GROUPS #############
class AlarmGroup(models.Model):
    aGroupName = models.CharField(max_length=300)
    aGroupRepeat = models.BooleanField(default=False, blank=True, null=True)
    aGroupDate = models.DateField(blank=True, null=True)
    aGroupDays = models.DateField(blank=True, null=True)
    # aGroupVibrate = models.BooleanField(default=True)
    aGroupSilent = models.BooleanField(default=False, blank=True, null=True)
    ringtone = models.ForeignKey(Ringtone, on_delete=models.PROTECT, blank=True, null=True)
    aGroupVolume = models.IntegerField(blank=True, null=True)
    # aGroupIncreaseVolume = models.BooleanField(default=False, blank=True, null=True)
    aGroupIsEnabled = models.BooleanField(default=True)
    

    def __str__(self):
        return f'{self.aGroupName}'

############# ALARMS #############
class Alarm(models.Model):
    alarmName = models.CharField(max_length=300)
    alarmTime = models.TimeField()
    alarmIsEnabled = models.BooleanField(default=True)
    alarmRepeat = models.BooleanField(default=False, blank=True, null=True)
    alarmDate = models.DateField(blank=True, null=True)
    alarmDays = models.CharField(max_length=100, blank=True, null=True)
    alarmSilent = models.BooleanField(default=False, blank=True, null=True)
    alarmVolume = models.IntegerField(blank=True, null=True)
    snoozeTime = models.IntegerField(blank=True, null=True)
    vibration = models.BooleanField(default=False, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    ringtone = models.ForeignKey(Ringtone, on_delete=models.PROTECT, blank=True, null=True)

    alarmGroup = models.ForeignKey(
      AlarmGroup, on_delete=models.SET_NULL, related_name='alarms', blank=True, null=True)
    @property
    def alarmInGroup(self):
        if self.alarmGroup:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.alarmName}'



############# TIMER GROUPS #############

class TimerGroup(models.Model):
  tGroupName = models.CharField()
  # tGroupVibrate = models.BooleanField(default=True)
  tGroupSilent = models.BooleanField(default=False)
  tGroupRingtone = models.IntegerField()
  tGroupVolume = models.IntegerField()
  # tGroupIncreaseVolume = models.BooleanField(default=False)
  tGroupIsEnabled = models.BooleanField(default=True)

def __str__(self):
  return f'{self.tGroupName}'


############# TIMERS #############

class Timer(models.Model):
  timerName = models.CharField()
  timerLength = models.TimeField()
  # timerVibrate = models.BooleanField(default=True)
  timerSilent = models.BooleanField(default=False)
  ringtone = models.ForeignKey(
      Ringtone, on_delete=models.PROTECT, blank=True, null=True)
  timerVolume = models.IntegerField()
  # timerIncreaseVolume = models.BooleanField(default=False)
  timerInGroup = models.BooleanField(default=False)
  timerGroup = models.ForeignKey(
    TimerGroup, on_delete=models.CASCADE, related_name='timer')
  timerIsEnabled = models.BooleanField(default=True)

  def __str__(self):
      return f'{self.timerName}'



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
