# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-24 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('receipt_no', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='receipt',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.Invoice'),
        ),
    ]
