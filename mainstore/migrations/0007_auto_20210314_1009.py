# Generated by Django 3.1.7 on 2021-03-14 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainstore', '0006_auto_20210314_1002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='discount',
            new_name='new_price',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='price',
            new_name='old_price',
        ),
    ]
