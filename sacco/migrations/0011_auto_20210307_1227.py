# Generated by Django 3.1.4 on 2021-03-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0010_auto_20210307_1033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article',
            new_name='article_paragraph1',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='sub_head_line',
            new_name='sub_head_line1',
        ),
        migrations.AddField(
            model_name='article',
            name='article_paragraph2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='article_paragraph3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='blockquote1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='blockquote2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='blockquote3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='sub_head_line2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='sub_head_line3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='head_line',
            field=models.CharField(max_length=200),
        ),
    ]
