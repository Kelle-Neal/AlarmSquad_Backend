from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
  #birthday = models.DateField(null = True)
  pass
  
  def __str__(self):
    return self.username


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
      


class Alarm(models.Model):
  name = models.CharField(max_length=300)
  whatTime = models.TimeField()
  repeat = models.BooleanField(default=False)
  whatDate = models.DateField()
  whatDays = models.DateField()
  snooze = models.BooleanField(default=False)
  # vibrate = models.BooleanField(default=True)
  silent = models.BooleanField(default=False)
  ringtone = models.IntegerField()
  volume = models.IntegerField()
  # increaseVolume = models.BooleanField(default=False)
  inGroup = models.BooleanField(default=False)
  group = models.IntegerField()
  isEnabled = models.BooleanField(default=True)

  def __str__(self):
    return f'{self.name}'


# class alarmGroup(models.Model):
#   name = models.CharField()
#   repeat = models.BooleanField(default=False)
#   whatDate = models.DateField()
#   whatDays = models.DateField()
#    # vibrate = models.BooleanField(default=True)
#   silent = models.BooleanField(default=False)
#   ringtone = models.IntegerField()
#   volume = models.IntegerField()
#   # increaseVolume = models.BooleanField(default=False)
#   isEnabled = models.BooleanField(default=True)

#   def __str__(self):
#     return f'{self.name}'

# class alarmToGroupBridge(models.Model):
#   alarmId = models.IntegerField()
#   alarmGroupId = models.IntegerField()

#   def __str__(self):
#     return f'{self.name}'

  # class timer(models.Model): 
  #   name = models.CharField()
  #   length = models.TimeField()
  #   # vibrate = models.BooleanField(default=True)
  #   silent = models.BooleanField(default=False)
  #   ringtone = models.IntegerField()
  #   volume = models.IntegerField()
  #   # increaseVolume = models.BooleanField(default=False)
  #   inGroup = models.BooleanField(default=False)
  #   group = models.IntegerField()
  #   isEnabled = models.BooleanField(default=True)

  #   def __str__(self):
  #     return f'{self.name}'

  # class timerGroup(models.Model):
  #   name = models.CharField()
  #   # vibrate = models.BooleanField(default=True)
  #   silent = models.BooleanField(default=False)
  #   ringtone = models.IntegerField()
  #   volume = models.IntegerField()
  #   # increaseVolume = models.BooleanField(default=False)    
  #   isEnabled = models.BooleanField(default=True)

  # def __str__(self):
  #   return f'{self.name}'

  # class timerToGroupBridge(mdoels.Model):
  #   timerId = models.IntegerField()
  #   timerGroupId = models.IntegerField()

  # def __str__(self):
  #   return f'{self.name}'


  # class ringtones(models.Model):
  #   name = models.CharField()

  # def __str__(self):
  #   return f'{self.name}'


  # class alertTypes(models.Model):
  #   alarmAlert = models.IntegerField()
  #   alarmGroupAlert = models.IntegerField()
  #   timerAlert = models.IntegerField()
  #   timerGroupAlert = models.IntegerField()

  # def __str__(self):
  #   return f'{self.name}'


  # class typeOfAlert(models.Model):
  #   name = models.CharField()

  # def __str__(self):
  #   return f'{self.name}'  


  # class notifications(models.Model):
  #   alert = models.IntegerField()
  #   alertType = models.IntegerField()
  #   user = models.IntegerField()

  # def __str__(self):
  #   return f'{self.name}'  
  

  
  