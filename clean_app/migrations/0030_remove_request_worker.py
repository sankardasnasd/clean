# Generated by Django 3.0 on 2023-09-18 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clean_app', '0029_pickup_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='WORKER',
        ),
    ]
