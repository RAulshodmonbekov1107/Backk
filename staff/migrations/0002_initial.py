# Generated by Django 5.0 on 2024-01-11 23:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
        ('user_authentication', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='user_authentication.address'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='emergency_contacts', to=settings.AUTH_USER_MODEL),
        ),
    ]
