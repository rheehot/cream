# Generated by Django 2.2.14 on 2020-07-17 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0004_week_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialInstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ofx_endpoint', models.URLField(max_length=500)),
                ('user_id', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('bank_id', models.CharField(max_length=100)),
                ('org', models.CharField(default='ISC', max_length=10)),
                ('fid', models.CharField(max_length=10)),
                ('version', models.IntegerField(default=220)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('memo', models.CharField(max_length=1000)),
                ('amount', models.FloatField()),
                ('date_posted', models.DateField()),
                ('check_number', models.IntegerField(null=True)),
                ('transaction_type', models.CharField(choices=[('CREDIT', 'credit'), ('DEBIT', 'debit'), ('INT', 'interest paid'), ('DIV', 'dividend'), ('FEE', 'financial institution fee'), ('SRVCHG', 'service charge'), ('DEP', 'deposit'), ('ATM', 'atm debit or credit'), ('POS', 'point of sale debit of credit'), ('XFER', 'transfer'), ('CHECK', 'check'), ('PAYMENT', 'electronic payment'), ('CASH', 'cash withdrawal'), ('DIRECTDEP', 'direct deposit'), ('DIRECTDEBIT', 'merchant initiated debit'), ('REPEATPMT', 'repeat payment'), ('HOLD', 'amount is under a hold'), ('OTHER', 'other'), ('CREDIT', 'credit')], max_length=11)),
            ],
        ),
        migrations.RemoveField(
            model_name='expense',
            name='actual_amount',
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(max_length=255)),
                ('account_number', models.CharField(max_length=100)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cash.FinancialInstitution')),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='transaction',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cash.Transaction'),
        ),
    ]
