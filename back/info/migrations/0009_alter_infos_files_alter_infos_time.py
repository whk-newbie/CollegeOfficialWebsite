# Generated by Django 4.0 on 2022-02-20 07:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infos',
            name='files',
            field=models.FileField(blank=True, default=None, null=True, upload_to='info/files', verbose_name='文件'),
        ),
        migrations.AlterField(
            model_name='infos',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间'),
        ),
    ]
