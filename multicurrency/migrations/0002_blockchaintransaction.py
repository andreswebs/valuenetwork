# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-21 04:31


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('valueaccounting', '0014_auto_20191218_0039'),
        ('multicurrency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockchainTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tx_hash', models.CharField(editable=False, max_length=96, verbose_name='Transaction Hash')),
                ('from_address', models.CharField(blank=True, max_length=128, null=True, verbose_name='From Address')),
                ('to_address', models.CharField(blank=True, max_length=128, null=True, verbose_name='To Address')),
                ('tx_fee', models.DecimalField(decimal_places=9, default=0, max_digits=20, verbose_name='Transaction Fee')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='chain_transaction', to='valueaccounting.EconomicEvent', verbose_name='event')),
            ],
        ),
    ]
