# Generated by Django 3.0.8 on 2021-03-07 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0006_article_sacco'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='sacco',
            new_name='publisher',
        ),
        migrations.AddField(
            model_name='article',
            name='last_accessed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
