# Generated by Django 5.0 on 2024-01-08 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_alter_patient_address_1_and_more'),
        ('user_authentication', '0003_address_baseuser_date_of_birth_baseuser_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='address_1',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='emergency_contact_1',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='emergency_contact_2',
        ),
        migrations.AddField(
            model_name='patient',
            name='primary_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_address', to='user_authentication.address'),
        ),
        migrations.AddField(
            model_name='patient',
            name='primary_emergency_contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_emergency_contact', to='patient.emergencycontact'),
        ),
        migrations.AddField(
            model_name='patient',
            name='secondary_emergency_contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_emergency_contact', to='patient.emergencycontact'),
        ),
    ]
