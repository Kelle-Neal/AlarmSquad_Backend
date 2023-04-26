# Generated by Django 4.2 on 2023-04-26 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alarmsquadAPI', '0005_alarmgroup_alarmtogroupbridge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alarmgroup',
            old_name='whatDate',
            new_name='aGroupDate',
        ),
        migrations.RenameField(
            model_name='alarmgroup',
            old_name='whatDays',
            new_name='aGroupDays',
        ),
        migrations.RenameField(
            model_name='alarmgroup',
            old_name='isEnabled',
            new_name='aGroupIsEnabled',
        ),
        migrations.RenameField(
            model_name='alarmgroup',
            old_name='label',
            new_name='aGroupName',
        ),
        migrations.RenameField(
            model_name='alarmgroup',
            old_name='repeat',
            new_name='aGroupRepeat',
        ),
        migrations.RenameField(
            model_name='alarmgroup',
            old_name='ringtone',
            new_name='aGroupRingtone',
        ),
        migrations.RenameField(
            model_name='alarmgroup',
            old_name='silent',
            new_name='aGroupSilent',
        ),
        migrations.RenameField(
            model_name='alarmgroup',
            old_name='volume',
            new_name='aGroupVolume',
        ),
    ]
