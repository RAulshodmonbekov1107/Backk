# Generated by Django 5.0 on 2024-02-24 11:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        ('user_authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergencycontact',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emergency_contacts', to='user_authentication.address'),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed'), ('separated', 'Separated'), ('divorced', 'Divorced'), ('common_law', 'Common-Law')], default='single', max_length=64)),
                ('primary_emergency_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_emergency_contact', to='patient.emergencycontact')),
                ('secondary_emergency_contact', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_emergency_contact', to='patient.emergencycontact')),
            ],
            options={
                'abstract': False,
            },
            bases=('user_authentication.baseuser',),
        ),
    ]
