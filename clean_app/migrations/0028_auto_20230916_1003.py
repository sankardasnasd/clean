# Generated by Django 3.0 on 2023-09-16 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clean_app', '0027_auto_20230916_1002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordersub',
            old_name='order_date',
            new_name='qty',
        ),
    ]
