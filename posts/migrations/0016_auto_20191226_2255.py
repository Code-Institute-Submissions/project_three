# Generated by Django 2.2.7 on 2019-12-26 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20191226_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='disseases',
            new_name='diseases',
        ),
    ]
