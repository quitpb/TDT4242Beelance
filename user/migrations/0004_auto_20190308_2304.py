# Generated by Django 2.0.6 on 2019-03-08 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='writtenBy',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
