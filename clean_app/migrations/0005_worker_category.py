# Generated by Django 3.0 on 2023-08-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clean_app', '0004_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
