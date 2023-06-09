# Generated by Django 4.2.1 on 2023-06-28 10:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_otherimagefile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Push_Meta_Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('orgid', models.CharField(blank=True, max_length=20, null=True)),
                ('userid', models.CharField(blank=True, max_length=20, null=True)),
                ('patiant', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('date', models.DateField(default=datetime.date.today)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pushed_File_Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('filename', models.CharField(blank=True, max_length=100, null=True)),
                ('filesize', models.CharField(blank=True, max_length=100, null=True)),
                ('stydyinstanceUID', models.CharField(blank=True, max_length=100, null=True)),
                ('parentpatienintances', models.CharField(blank=True, max_length=100, null=True)),
                ('parentstudy', models.CharField(blank=True, max_length=100, null=True)),
                ('orgid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organisation')),
            ],
        ),
    ]
