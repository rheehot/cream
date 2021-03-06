# Generated by Django 3.0.8 on 2020-07-31 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0015_transfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialinstitution',
            name='bank_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='financialinstitution',
            name='fid',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='financialinstitution',
            name='ofx_endpoint',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='financialinstitution',
            name='org',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='financialinstitution',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='financialinstitution',
            name='user_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='financialinstitution',
            name='version',
            field=models.IntegerField(blank=True, default=220, null=True),
        ),
    ]
