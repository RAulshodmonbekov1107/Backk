# Generated by Django 5.0 on 2024-02-05 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0002_rename_individual_unique_number_baseuser_inn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='inn',
            field=models.CharField(primary_key=True, serialize=False, unique=True),
        ),
    ]
