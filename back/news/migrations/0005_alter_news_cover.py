# Generated by Django 4.0 on 2022-04-23 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0004_alter_news_body_alter_news_cover_delete_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='cover/%Y%m%d', verbose_name='封面'),
        ),
    ]
