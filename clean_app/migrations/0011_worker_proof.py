# Generated by Django 3.0 on 2023-08-18 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clean_app', '0010_auto_20230818_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='proof',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]