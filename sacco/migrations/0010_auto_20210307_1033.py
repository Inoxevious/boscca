# Generated by Django 3.1.4 on 2021-03-07 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0009_auto_20210307_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='head_line',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='sub_head_line',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]