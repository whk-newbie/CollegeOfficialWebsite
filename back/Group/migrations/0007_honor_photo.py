# Generated by Django 4.0 on 2022-05-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0006_honor_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='honor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='honor', verbose_name='封面图片'),
        ),
    ]