# Generated by Django 3.1.4 on 2021-01-06 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infoabouttek',
            name='infoshort',
        ),
    ]
