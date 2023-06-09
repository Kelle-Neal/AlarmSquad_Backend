# Generated by Django 4.2 on 2023-04-28 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarmsquadAPI', '0011_timergroup_remove_alarm_alarmringtone_alarm_ringtone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarm',
            name='alarmSnooze',
        ),
        migrations.AddField(
            model_name='alarm',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='alarm',
            name='snoozeTime',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='alarm',
            name='vibration',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='alarmDays',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
