# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nsaid', '0003_delete_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=100)),
                ('vet_url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('petsid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('breed', models.CharField(max_length=100)),
                ('pic_url', models.CharField(max_length=500)),
                ('city', models.ForeignKey(to='nsaid.City', related_name='city')),
            ],
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('shelterid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('hours', models.CharField(max_length=200)),
                ('city', models.ForeignKey(to='nsaid.City')),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='shelter',
            field=models.ForeignKey(to='nsaid.Shelter'),
        ),
    ]
