# Generated by Django 4.2 on 2023-04-27 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarmsquadAPI', '0009_alter_alarm_alarmgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ringtone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('soundFile', models.FileField(upload_to='ringtones/')),
            ],
        ),
    ]