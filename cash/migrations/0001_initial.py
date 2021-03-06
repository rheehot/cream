# Generated by Django 2.1.2 on 2018-10-06 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budgeted_amount', models.FloatField()),
                ('actual_amount', models.FloatField(null=True)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.FloatField()),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cash.Week'),
        ),
    ]
