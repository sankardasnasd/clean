# Generated by Django 3.0 on 2023-09-16 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clean_app', '0024_auto_20230916_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermain',
            name='RECYCLE',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clean_app.Recycle'),
        ),
    ]
