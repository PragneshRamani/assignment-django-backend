# Generated by Django 3.2.13 on 2022-04-27 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('transaction_type', models.CharField(blank=True, choices=[('Borrows', 'Borrows'), ('Lendes', 'Lendes')], max_length=128, null=True)),
                ('transaction_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('transaction_status', models.CharField(blank=True, choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')], max_length=128, null=True)),
                ('transaction_with', models.CharField(blank=True, max_length=255, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('transaction_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Transaction',
                'verbose_name_plural': 'User Transactions',
            },
        ),
        migrations.CreateModel(
            name='UserBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=11)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Balance',
                'verbose_name_plural': 'User Balances',
            },
        ),
    ]
