# Generated by Django 5.0.3 on 2024-05-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_room_evaluation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.FloatField(max_length=100),
        ),
    ]
