# Generated by Django 4.0.5 on 2022-06-28 23:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0005_alter_asleep_asleep_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asleep',
            name='asleep_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 28, 23, 48, 21, 176632)),
        ),
    ]