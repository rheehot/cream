# Generated by Django 3.0.8 on 2020-08-02 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0017_auto_20200731_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payperiod',
            old_name='transactions',
            new_name='paychecks',
        ),
    ]
