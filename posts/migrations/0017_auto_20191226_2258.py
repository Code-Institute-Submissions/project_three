# Generated by Django 2.2.7 on 2019-12-26 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_auto_20191226_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='water',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='feeding',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
    ]
