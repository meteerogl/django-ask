# Generated by Django 2.1 on 2018-08-31 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20180831_2040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='kullanıcı',
            new_name='username',
        ),
    ]
