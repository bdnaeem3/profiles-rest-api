# Generated by Django 2.2.7 on 2019-11-13 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_stuff',
            new_name='is_staff',
        ),
    ]
