# Generated by Django 3.1.7 on 2021-03-22 18:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainstore', '0023_wishlist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WishList',
            new_name='UserWishList',
        ),
    ]
