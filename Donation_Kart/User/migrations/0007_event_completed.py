# Generated by Django 2.1 on 2019-04-13 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_auto_20190414_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]