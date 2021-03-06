# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-12 17:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20180211_0022'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('office', '0012_bus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_as', models.CharField(blank=True, max_length=255, null=True)),
                ('month', models.CharField(blank=True, max_length=255, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('paid_amount', models.FloatField(blank=True, null=True)),
                ('payment_status', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Class')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.School')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Section')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payer', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
