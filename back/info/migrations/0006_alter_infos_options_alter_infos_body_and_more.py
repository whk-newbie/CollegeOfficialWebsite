# Generated by Django 4.0 on 2022-01-24 08:25

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_alter_infos_files'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infos',
            options={'verbose_name': '学院通知', 'verbose_name_plural': '通知列表'},
        ),
        migrations.AlterField(
            model_name='infos',
            name='body',
            field=mdeditor.fields.MDTextField(verbose_name='通知内容'),
        ),
        migrations.AlterField(
            model_name='infos',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
    ]