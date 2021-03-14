# Generated by Django 3.1.7 on 2021-03-14 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstore', '0005_auto_20210314_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='manufacture',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='upcoming_product',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
