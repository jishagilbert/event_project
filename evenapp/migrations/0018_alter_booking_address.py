# Generated by Django 5.0.4 on 2024-04-23 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evenapp', '0017_rename_client_service_services_remove_services_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
