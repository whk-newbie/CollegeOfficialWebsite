# Generated by Django 4.0 on 2022-05-06 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0004_rename_date_achievements_create_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='achievements',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='institutions',
            old_name='name',
            new_name='title',
        ),
    ]
