# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 05:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_survey'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='questions.Survey'),
            preserve_default=False,
        ),
    ]
