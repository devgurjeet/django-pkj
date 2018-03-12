# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-12 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbm', '0002_contacts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name_plural': 'contacts'},
        ),
        migrations.AlterField(
            model_name='contacts',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_contact_set', to='bbm.Pins'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='pin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_set', to='bbm.Pins'),
        ),
        migrations.AlterUniqueTogether(
            name='contacts',
            unique_together=set([('pin', 'contact')]),
        ),
    ]