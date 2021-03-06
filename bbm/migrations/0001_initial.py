# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-12 08:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PinMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_key', models.CharField(max_length=100)),
                ('meta_value', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Pins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'pins',
            },
        ),
        migrations.AddField(
            model_name='pinmeta',
            name='pin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbm.Pins'),
        ),
    ]
