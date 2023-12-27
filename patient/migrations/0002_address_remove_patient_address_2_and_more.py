# Generated by Django 5.0 on 2023-12-27 13:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='address_2',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='emergency_contact_2',
        ),
        migrations.AlterField(
            model_name='patient',
            name='address_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_1', to='patient.address'),
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=32)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='patient.address')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emergency_contacts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='emergency_contact_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emergency_contact_1', to='patient.emergencycontact'),
        ),
    ]
