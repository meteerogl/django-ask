# Generated by Django 2.1 on 2018-09-16 13:35

import accounts.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_auto_20180910_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='p_photo',
            field=models.ImageField(default=datetime.datetime(2018, 9, 16, 13, 35, 38, 469432, tzinfo=utc),  verbose_name='ProfilePhoto'),
            preserve_default=False,
        ),
    ]
