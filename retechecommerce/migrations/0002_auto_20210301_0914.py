# Generated by Django 3.1.6 on 2021-03-01 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retechecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufactures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(default='images/manafactures/default.png', upload_to='images/manufactures')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='discount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='pic',
            field=models.ImageField(default='images/items/default.png', upload_to='images/items'),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]