# Generated by Django 5.0.4 on 2024-04-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evenapp', '0018_alter_booking_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='address',
            field=models.TextField(),
        ),
    ]
