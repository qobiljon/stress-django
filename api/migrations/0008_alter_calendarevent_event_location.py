# Generated by Django 4.1.3 on 2022-11-29 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_calendarevent_event_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevent',
            name='event_location',
            field=models.CharField(max_length=256, null=True),
        ),
    ]