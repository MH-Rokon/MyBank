# Generated by Django 5.0.6 on 2024-05-31 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0007_rename_aceecess_transaction_access'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='access',
        ),
        migrations.AddField(
            model_name='transaction',
            name='loan_approve',
            field=models.BooleanField(default=False),
        ),
    ]