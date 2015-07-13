# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nsaid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=100)),
                ('vet_url', models.CharField(max_length=500)),
            ],
        ),
    ]
