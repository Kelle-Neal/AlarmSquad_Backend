from django.contrib import admin
from .models import *

class AlarmAdmin(admin.ModelAdmin):
  list_display = ('alarmName', 'alarmTime')


admin.site.register(CustomUser)
admin.site.register(Alarm)
admin.site.register(AlarmGroup)
admin.site.register(Ringtone)

#321_LetsGo