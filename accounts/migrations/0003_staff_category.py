# Generated by Django 3.1.7 on 2021-03-23 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210323_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='category',
            field=models.CharField(choices=[('CEO', 'CEO'), ('Manager', 'Manager'), ('Customer Manager', 'Customer Manager')], default='CEO', max_length=255),
            preserve_default=False,
        ),
    ]
