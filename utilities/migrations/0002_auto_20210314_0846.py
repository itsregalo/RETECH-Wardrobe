# Generated by Django 3.1.7 on 2021-03-14 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryimage',
            options={'verbose_name': 'Category Image', 'verbose_name_plural': 'Category Images'},
        ),
        migrations.AlterField(
            model_name='categoryimage',
            name='image',
            field=models.ImageField(upload_to='images/utilities/category'),
        ),
        migrations.AlterField(
            model_name='newproductcollection',
            name='image',
            field=models.ImageField(upload_to='images/utilities/NewProductCollection'),
        ),
    ]
