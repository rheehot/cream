# Generated by Django 3.0.10 on 2020-10-10 13:11

from django.db import migrations, models
import recurrence.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0021_auto_20201009_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='budgeted_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='recurrences',
            field=recurrence.fields.RecurrenceField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payperiod',
            name='recurrences',
            field=recurrence.fields.RecurrenceField(blank=True, null=True),
        ),
    ]
