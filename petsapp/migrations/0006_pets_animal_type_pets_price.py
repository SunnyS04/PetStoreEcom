# Generated by Django 4.2.1 on 2023-06-20 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsapp', '0005_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='animal_type',
            field=models.CharField(choices=[('D', 'Dog'), ('C', 'Cat')], default='NA', max_length=25),
        ),
        migrations.AddField(
            model_name='pets',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]