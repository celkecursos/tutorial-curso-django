# Generated by Django 5.1.4 on 2024-12-31 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_financial_transactions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': 'transação', 'verbose_name_plural': 'transações'},
        ),
    ]
