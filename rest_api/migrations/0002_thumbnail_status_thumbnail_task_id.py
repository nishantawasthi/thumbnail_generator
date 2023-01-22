# Generated by Django 4.1.5 on 2023-01-22 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbnail',
            name='status',
            field=models.IntegerField(choices=[(1, 'PENDING'), (2, 'SUCCESS'), (3, 'FAILED')], null=True),
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='task_id',
            field=models.CharField(max_length=500, null=True, unique=True),
        ),
    ]