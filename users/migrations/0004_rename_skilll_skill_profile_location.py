# Generated by Django 5.1.5 on 2025-02-07 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_skilll'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skilll',
            new_name='Skill',
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
