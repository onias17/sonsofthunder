# Generated by Django 3.1.4 on 2020-12-16 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20201215_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='building_type',
            field=models.CharField(choices=[('R', 'Residential'), ('C', 'Commercial'), ('I', 'Industrial')], max_length=1, verbose_name='Building Type'),
        ),
    ]
