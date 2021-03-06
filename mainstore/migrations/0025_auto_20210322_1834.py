# Generated by Django 3.1.7 on 2021-03-22 18:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainstore', '0024_auto_20210322_1831'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userwishlist',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Wishlist', 'verbose_name_plural': 'Wishlists'},
        ),
        migrations.AlterModelOptions(
            name='wishlistitem',
            options={'ordering': ['-timestamp'], 'verbose_name': 'wishlist item', 'verbose_name_plural': 'Wishlist Items'},
        ),
        migrations.AlterUniqueTogether(
            name='userwishlist',
            unique_together={('user',)},
        ),
    ]
