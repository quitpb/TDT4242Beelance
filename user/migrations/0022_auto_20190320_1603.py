# Generated by Django 2.0.6 on 2019-03-20 16:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_auto_20190320_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 3, 20, 16, 3, 19, 699164, tzinfo=utc)),
        ),
    ]