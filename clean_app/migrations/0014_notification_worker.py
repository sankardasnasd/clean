# Generated by Django 3.0 on 2023-08-20 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clean_app', '0013_allocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='WORKER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clean_app.Worker'),
            preserve_default=False,
        ),
    ]
