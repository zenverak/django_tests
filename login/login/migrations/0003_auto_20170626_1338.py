# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_randids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randids',
            name='id_number',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]