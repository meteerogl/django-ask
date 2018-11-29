# Generated by Django 2.1 on 2018-08-31 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0028_auto_20180831_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='COUPLING',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matched_user', models.CharField(max_length=25, verbose_name='matched')),
                ('match_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'COUPLING',
                'ordering': ['match_user'],
            },
        ),
    ]