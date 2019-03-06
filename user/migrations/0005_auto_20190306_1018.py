# Generated by Django 2.0.6 on 2019-03-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190306_0951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='display_email_name',
            new_name='display_email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='display_last_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='display_city',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='display_company',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='display_postal',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='display_state',
            field=models.BooleanField(default=True),
        ),
    ]
