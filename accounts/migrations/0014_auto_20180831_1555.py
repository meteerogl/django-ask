# Generated by Django 2.1 on 2018-08-31 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20180831_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='kullanıcı',
        ),
    ]