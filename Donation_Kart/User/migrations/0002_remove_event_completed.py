# Generated by Django 2.1 on 2019-04-30 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='completed',
        ),
    ]
