# Generated by Django 2.2.7 on 2019-12-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_auto_20191227_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]