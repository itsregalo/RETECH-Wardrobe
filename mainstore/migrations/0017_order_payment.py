# Generated by Django 3.1.7 on 2021-03-19 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainstore', '0016_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainstore.payment'),
        ),
    ]
