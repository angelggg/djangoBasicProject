# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-11-04 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geostats', '0002_auto_20201104_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='capital',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='capital_of', to='geostats.Town'),
        ),
    ]