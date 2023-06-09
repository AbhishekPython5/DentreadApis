# Generated by Django 4.2.1 on 2023-06-05 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_iosfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherImageFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('parent_orgid', models.CharField(blank=True, max_length=200, null=True)),
                ('repid', models.IntegerField(blank=True, null=True)),
                ('sodrid', models.IntegerField(blank=True, null=True)),
                ('topid', models.IntegerField(blank=True, null=True)),
                ('pid', models.IntegerField(blank=True, null=True)),
                ('file', models.FileField(upload_to='otherFile/')),
                ('size', models.IntegerField(blank=True, null=True)),
                ('fileName', models.CharField(blank=True, max_length=100, null=True)),
                ('fileStatus', models.CharField(blank=True, max_length=100, null=True)),
                ('fileComment', models.CharField(blank=True, max_length=100, null=True)),
                ('thumbnail', models.ImageField(upload_to='static/otherThumb/')),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'db_table': 'dent_otherimagefile',
                'managed': False,
            },
        ),
    ]
