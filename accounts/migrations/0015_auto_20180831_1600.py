# Generated by Django 2.1 on 2018-08-31 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20180831_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='kullanıcı',
            new_name='user',
        ),
    ]