# Generated by Django 3.0.8 on 2021-02-24 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210224_0534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('course_name', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('course_length', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('lead_tutor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lead_tutor', to='users.Tutor', verbose_name='Tutor')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_id', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('module_name', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('decription', models.TextField(blank=True, null=True)),
                ('intro', models.TextField(blank=True, null=True)),
                ('module_length', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('upload_date', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='users.Course', verbose_name='Course')),
                ('tutor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='module_tutor', to='users.Tutor', verbose_name='Tutor')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_id', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('survey_name', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
                ('survey', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey', to='users.Survey', verbose_name='Survey')),
            ],
        ),
        migrations.CreateModel(
            name='ModuleItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='module', to='users.Module', verbose_name='Course')),
            ],
        ),
    ]
