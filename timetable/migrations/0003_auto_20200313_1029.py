# Generated by Django 2.2.10 on 2020-03-13 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20200310_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='busy',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='owner',
        ),
    ]