# Generated by Django 5.0 on 2023-12-27 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baseuser',
            options={},
        ),
        migrations.AlterModelManagers(
            name='baseuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='baseuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='baseuser',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='baseuser',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='baseuser',
            name='id',
        ),
        migrations.RemoveField(
            model_name='baseuser',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='baseuser',
            name='username',
        ),
        migrations.AddField(
            model_name='baseuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='individual_unique_number',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]
