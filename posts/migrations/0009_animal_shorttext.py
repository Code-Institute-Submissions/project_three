# Generated by Django 2.2.7 on 2019-11-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20191123_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='shorttext',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
