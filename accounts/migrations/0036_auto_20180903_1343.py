# Generated by Django 2.1 on 2018-09-03 13:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0035_like_questions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LIKE_QUESTIONS',
            new_name='LIKE',
        ),
    ]
