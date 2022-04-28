# Generated by Django 4.0 on 2022-04-25 08:50

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='author',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='info_author', to='auth.user', verbose_name='发布者'),
        ),
        migrations.AlterField(
            model_name='information',
            name='content',
            field=mdeditor.fields.MDTextField(blank=True, verbose_name='内容'),
        ),
    ]