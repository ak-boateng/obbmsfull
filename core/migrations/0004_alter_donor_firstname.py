# Generated by Django 4.1.7 on 2023-04-30 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_donor_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='firstname',
            field=models.CharField(max_length=30),
        ),
    ]
