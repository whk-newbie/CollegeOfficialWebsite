# Generated by Django 4.0 on 2022-04-30 02:16

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartyFileAndTrends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('category', models.CharField(choices=[('教育文件', '教育文件'), ('学习动态', '学习动态')], max_length=100, verbose_name='分类')),
                ('content', mdeditor.fields.MDTextField(verbose_name='内容')),
                ('file', models.FileField(blank=True, upload_to='party/files/', verbose_name='文件')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '党史教育文件及动态',
                'verbose_name_plural': '党史教育文件及动态',
            },
        ),
        migrations.AlterField(
            model_name='partybuilding',
            name='content',
            field=mdeditor.fields.MDTextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='partybuilding',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='partybuilding',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
    ]
