# Generated by Django 4.0.5 on 2022-06-28 21:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_remove_asleep_last_modified_alter_asleep_asleep_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asleep',
            name='asleep_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 28, 23, 12, 21, 392043)),
        ),
    ]