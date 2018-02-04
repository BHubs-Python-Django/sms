# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-03 04:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0012_auto_20180201_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Class')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=222)),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_dashboard.Subject'),
        ),
    ]