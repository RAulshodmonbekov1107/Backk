# Generated by Django 5.0.4 on 2024-05-06 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='branch_administrator',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='branch_administrator', to='staff.branchadministrator'),
        ),
        migrations.AddField(
            model_name='branch',
            name='director',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='director', to='staff.doctor'),
        ),
        migrations.AddField(
            model_name='branch',
            name='doctors',
            field=models.ManyToManyField(related_name='doctors', to='staff.doctor'),
        ),
        migrations.AddField(
            model_name='branch',
            name='patient_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_manager', to='staff.patientmanager'),
        ),
        migrations.AddField(
            model_name='branch',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='hospital.branchaddress'),
        ),
        migrations.AddField(
            model_name='branch',
            name='phone_numbers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phone_numbers', to='hospital.branchphonenumber'),
        ),
        migrations.AddField(
            model_name='department',
            name='branches',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='hospital.branch'),
        ),
        migrations.AddField(
            model_name='department',
            name='head',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department_head', to='staff.doctor'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_administrator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hospital_administrator', to='staff.hospitaladministrator'),
        ),
        migrations.AddField(
            model_name='branch',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='hospital.hospital'),
        ),
    ]
