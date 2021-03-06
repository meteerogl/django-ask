# Generated by Django 2.1 on 2018-08-21 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ACCOUNTS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=70, verbose_name='E Mail')),
                ('name', models.CharField(max_length=25, verbose_name='Name')),
                ('surname', models.CharField(max_length=25, verbose_name='Surname')),
                ('username', models.CharField(max_length=20, verbose_name='Username')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
                ('birthday', models.DateTimeField(verbose_name='Birthday')),
                ('gender', models.CharField(max_length=15)),
                ('language', models.CharField(max_length=20, verbose_name='language')),
            ],
            options={
                'verbose_name_plural': 'ACCOUNTS',
                'ordering': ['id'],
            },
        ),
    ]
