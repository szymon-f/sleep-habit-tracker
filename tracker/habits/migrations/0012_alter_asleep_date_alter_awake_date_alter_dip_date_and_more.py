# Generated by Django 4.0.5 on 2022-06-29 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0011_alter_asleep_date_alter_awake_date_alter_dip_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asleep',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 29, 20, 29, 22, 691632)),
        ),
        migrations.AlterField(
            model_name='awake',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 29, 20, 29, 22, 691777)),
        ),
        migrations.AlterField(
            model_name='dip',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 29, 20, 29, 22, 691895)),
        ),
        migrations.AlterField(
            model_name='dreamnote',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 29, 20, 29, 22, 692009)),
        ),
    ]
