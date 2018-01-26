# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-26 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('popisi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dokumentacija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opis', models.CharField(max_length=100)),
                ('vrsta_dokumenta', models.CharField(choices=[('ST', 'Standard'), ('SM', 'Smernice'), ('SL', 'Strokovna literatura')], default='ST', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PodrocjeSpecifikacije',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opis', models.CharField(max_length=100)),
                ('podrocje', models.CharField(max_length=100)),
                ('podrobnosti', models.CharField(max_length=100)),
                ('vrsta', models.CharField(choices=[('LM', 'Lastnosti materialov'), ('PD', 'Pogoji dela'), ('LI', 'Delovni postopki'), ('PI', 'Lastnosti izdelka'), ('VZ', 'Varnostne zahteve')], default='LM', max_length=10)),
                ('osnova', models.CharField(choices=[('Z', 'Zakonodaja'), ('P', 'Pravila stroke'), ('S', 'Smernice')], default='P', max_length=10)),
                ('dokumentacija', models.ManyToManyField(to='specifikacije.Dokumentacija')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PosebnoDolocilo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opis', models.CharField(max_length=100)),
                ('dela', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='popisi.Dela')),
                ('dokumentacija', models.ManyToManyField(to='specifikacije.Dokumentacija')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Specifikacija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opis', models.CharField(max_length=100)),
                ('podrocje_specifikacije', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='specifikacije.PodrocjeSpecifikacije')),
                ('postavka', models.ManyToManyField(to='popisi.Postavka')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SplosnoDolocilo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opis', models.CharField(max_length=100)),
                ('dokumentacija', models.ManyToManyField(to='specifikacije.Dokumentacija')),
                ('vrsta_del', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='popisi.VrstaDel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
