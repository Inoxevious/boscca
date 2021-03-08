# Generated by Django 3.1.4 on 2021-03-08 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0015_objective'),
        ('web', '0004_auto_20210307_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmembers',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sacco.nationalstaffmember'),
        ),
        migrations.AddField(
            model_name='homepagearticle',
            name='home_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.homepage'),
        ),
        migrations.AddField(
            model_name='homepagefacts',
            name='home_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.homepage'),
        ),
        migrations.AddField(
            model_name='homepageobjective',
            name='home_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.homepage'),
        ),
        migrations.AddField(
            model_name='homepageslider',
            name='home_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.homepage'),
        ),
        migrations.AddField(
            model_name='homepagetestimonial',
            name='home_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.homepage'),
        ),
    ]
