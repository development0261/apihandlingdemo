# Generated by Django 4.0.1 on 2022-01-07 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_staff_timestamp'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Staff',
            new_name='APIDATA',
        ),
    ]
