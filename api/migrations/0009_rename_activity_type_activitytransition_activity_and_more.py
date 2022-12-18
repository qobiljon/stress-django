# Generated by Django 4.1.3 on 2022-11-30 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_calendarevent_event_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activitytransition',
            old_name='activity_type',
            new_name='activity',
        ),
        migrations.RenameField(
            model_name='activitytransition',
            old_name='transition_type',
            new_name='transition',
        ),
        migrations.CreateModel(
            name='ActivityRecognition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.BigIntegerField(db_index=True)),
                ('activity', models.CharField(max_length=256)),
                ('confidence', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]