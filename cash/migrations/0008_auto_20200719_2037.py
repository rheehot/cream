# Generated by Django 2.2.14 on 2020-07-19 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0007_auto_20200717_2212'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Week',
            new_name='PayPeriod',
        ),
    ]
