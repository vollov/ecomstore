# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('name', models.CharField(max_length=60, unique=True, null=True)),
                ('code', models.CharField(max_length=10, unique=True, null=True)),
                ('currency_rate', models.DecimalField(default=5.0, max_digits=9, decimal_places=2, blank=True)),
                ('tax_rate', models.DecimalField(default=0.13, max_digits=9, decimal_places=2, blank=True)),
                ('agent_share', models.DecimalField(default=0.4, max_digits=9, decimal_places=2, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
