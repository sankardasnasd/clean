# Generated by Django 3.0 on 2023-09-16 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clean_app', '0023_bank'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bank',
            old_name='Accn',
            new_name='cardnumber',
        ),
        migrations.RenameField(
            model_name='bank',
            old_name='Ifsc',
            new_name='expiredate',
        ),
    ]