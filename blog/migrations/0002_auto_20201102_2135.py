# Generated by Django 3.1.2 on 2020-11-02 21:35

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
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 2, 21, 35, 8, 998532, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 2, 21, 35, 8, 997690, tzinfo=utc)),
        ),
    ]
