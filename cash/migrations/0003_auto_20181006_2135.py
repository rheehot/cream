# Generated by Django 2.1.2 on 2018-10-06 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0002_auto_20181006_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='_carry_over',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='actual_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
