# Generated by Django 4.1.2 on 2022-11-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offbody',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='selfreport',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
