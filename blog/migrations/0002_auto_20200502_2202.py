# Generated by Django 2.2.6 on 2020-05-02 16:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 5, 2, 16, 2, 9, 168839, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 16, 2, 9, 167838, tzinfo=utc)),
        ),
    ]
