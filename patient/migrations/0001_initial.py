# Generated by Django 5.0 on 2023-12-27 13:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_authentication', '0002_alter_baseuser_options_alter_baseuser_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(max_length=255)),
                ('emergency_contact_1', models.CharField(max_length=64)),
                ('emergency_contact_2', models.CharField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
            bases=('user_authentication.baseuser',),
        ),
    ]
