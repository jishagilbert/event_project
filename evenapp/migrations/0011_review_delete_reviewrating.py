# Generated by Django 5.0.4 on 2024-04-22 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evenapp', '0010_alter_reviewrating_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('rating', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='reviewrating',
        ),
    ]
