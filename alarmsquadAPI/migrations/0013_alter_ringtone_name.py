# Generated by Django 4.2 on 2023-04-28 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarmsquadAPI', '0012_remove_alarm_alarmsnooze_alarm_note_alarm_snoozetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ringtone',
            name='name',
            field=models.JSONField(),
        ),
    ]