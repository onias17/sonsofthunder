# Generated by Django 3.1.4 on 2021-01-08 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20201217_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='building_type',
            field=models.CharField(choices=[('Residential', 'Residential'), ('Commercial', 'Commercial'), ('Industrial', 'Industrial')], max_length=11, verbose_name='Building Type'),
        ),
    ]