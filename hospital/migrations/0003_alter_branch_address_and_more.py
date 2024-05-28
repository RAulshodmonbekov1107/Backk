# Generated by Django 5.0.4 on 2024-05-12 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_initial'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='branch', to='hospital.branchaddress'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='branch_administrator',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='branch', to='staff.branchadministrator'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='director',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='branch', to='staff.doctor'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='phone_numbers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='branch', to='hospital.branchphonenumber'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_administrator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hospital', to='staff.hospitaladministrator'),
        ),
    ]