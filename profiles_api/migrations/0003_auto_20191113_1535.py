# Generated by Django 2.2.7 on 2019-11-13 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_auto_20191113_1529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_staff',
            new_name='is_stuff',
        ),
    ]
