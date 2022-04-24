# Generated by Django 4.0 on 2022-04-18 11:33

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_alter_news_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=mdeditor.fields.MDTextField(verbose_name='文章内容'),
        ),
        migrations.AlterField(
            model_name='news',
            name='cover',
            field=models.ImageField(null=True, upload_to='cover/%Y%m%d'),
        ),
        migrations.DeleteModel(
            name='Cover',
        ),
    ]
