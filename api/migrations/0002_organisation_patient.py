# Generated by Django 4.2.1 on 2023-05-31 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('org_id', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 5, 31, 15, 6, 42, 400987))),
                ('orgname', models.CharField(max_length=200)),
                ('ctperson_name', models.CharField(blank=True, max_length=200, null=True)),
                ('manager', models.CharField(blank=True, max_length=200, null=True)),
                ('orgtype', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=20)),
                ('gstin', models.ImageField(blank=True, null=True, upload_to='static/gstFile/')),
                ('status', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=64, null=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('offered_service', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('pincode', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=30)),
                ('regby_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('regby_userid', models.IntegerField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='static/logo/')),
                ('pan', models.ImageField(blank=True, null=True, upload_to='static/panCard/')),
                ('cin', models.ImageField(blank=True, null=True, upload_to='static/cinNo/')),
                ('regFile', models.ImageField(blank=True, null=True, upload_to='static/regFile/')),
                ('bankName', models.CharField(blank=True, max_length=30)),
                ('accountNumber', models.IntegerField(blank=True, null=True)),
                ('ifscCode', models.CharField(blank=True, max_length=30)),
                ('customFile', models.ImageField(null=True, upload_to='static/cancelledCheque/')),
                ('paymentOption', models.CharField(blank=True, max_length=100, null=True)),
                ('topUp', models.IntegerField(blank=True, null=True)),
                ('topUpAvailable', models.IntegerField(blank=True, null=True)),
                ('preferredLab', models.CharField(blank=True, max_length=200, null=True)),
                ('connectionDate', models.DateField(blank=True, null=True)),
                ('pickup', models.CharField(blank=True, max_length=100, null=True)),
                ('admin', models.IntegerField(blank=True, null=True)),
                ('managerId', models.IntegerField(blank=True, null=True)),
                ('subscription', models.CharField(blank=True, default='Dentread Basic', max_length=100, null=True)),
                ('subscriptionId', models.IntegerField(blank=True, default=1, null=True)),
                ('pickuplocation', models.CharField(blank=True, max_length=100, null=True)),
                ('invoiceMonth', models.IntegerField(blank=True, default=0, null=True)),
                ('invoicePath', models.FileField(upload_to='static/orgInvoice/')),
                ('lab_connection', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'dent_organisation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pid', models.CharField(blank=True, max_length=200, null=True)),
                ('parent_orgid', models.CharField(blank=True, max_length=200, null=True)),
                ('locate', models.CharField(max_length=200)),
                ('regby', models.CharField(max_length=200)),
                ('rdate', models.DateField(default=datetime.date.today)),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(blank=True)),
                ('gender', models.CharField(max_length=6)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact', models.CharField(blank=True, max_length=20, null=True)),
                ('address_1', models.CharField(blank=True, max_length=128, null=True)),
                ('address_2', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(default='000000', max_length=5)),
                ('medih', models.CharField(max_length=800)),
                ('refdoctor', models.CharField(blank=True, max_length=50, null=True)),
                ('docid', models.IntegerField(blank=True, null=True)),
                ('reffor', models.CharField(max_length=300)),
                ('dcm_status', models.CharField(blank=True, max_length=50, null=True)),
                ('refptid', models.IntegerField(blank=True, null=True)),
                ('refpt_orgid', models.IntegerField(blank=True, null=True)),
                ('reforgid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dent_patient',
                'managed': False,
            },
        ),
    ]
