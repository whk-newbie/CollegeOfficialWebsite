# Generated by Django 4.0 on 2022-05-06 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0011_alter_recruiting_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recruiting',
            old_name='created',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='created',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='teachermorality',
            old_name='created',
            new_name='create_time',
        ),
    ]