# Generated by Django 3.1.6 on 2021-03-23 10:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogproject',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blogproject',
            name='url',
        ),
        migrations.AddField(
            model_name='blogproject',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 3, 23, 10, 34, 29, 145163, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogproject',
            name='description',
            field=models.TextField(max_length=250),
        ),
    ]