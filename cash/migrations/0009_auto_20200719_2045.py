# Generated by Django 2.2.14 on 2020-07-19 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0008_auto_20200719_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='week',
            new_name='payperiod',
        ),
    ]
