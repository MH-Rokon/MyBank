# Generated by Django 4.2.4 on 2024-01-03 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_alter_transaction_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='aceecess',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'Deposit'), (2, 'Withdrawal'), (3, 'Loan'), (4, 'Loan_Paid'), (5, 'SENDMONEY '), (6, 'RECEIVEMONEY ')], null=True),
        ),
    ]
