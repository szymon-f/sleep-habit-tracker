# Generated by Django 4.0.5 on 2022-07-09 22:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0013_alter_asleep_date_alter_awake_date_alter_dip_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asleep',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 9, 22, 19, 57, 307134)),
        ),
        migrations.AlterField(
            model_name='awake',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 9, 22, 19, 57, 307283)),
        ),
        migrations.AlterField(
            model_name='dip',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 9, 22, 19, 57, 307400)),
        ),
        migrations.AlterField(
            model_name='dreamnote',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 9, 22, 19, 57, 307504)),
        ),
    ]