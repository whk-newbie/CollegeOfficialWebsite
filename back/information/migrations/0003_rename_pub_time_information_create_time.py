# Generated by Django 4.0 on 2022-05-06 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_alter_information_author_alter_information_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='information',
            old_name='pub_time',
            new_name='create_time',
        ),
    ]
