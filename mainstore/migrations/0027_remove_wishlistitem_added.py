# Generated by Django 3.1.7 on 2021-03-22 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainstore', '0026_wishlistitem_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistitem',
            name='added',
        ),
    ]
