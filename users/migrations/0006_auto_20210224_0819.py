# Generated by Django 3.0.8 on 2021-02-24 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210224_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='moduleitems',
            name='upload_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('registration_date', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_course', to='users.Course', verbose_name='Course')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Department')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Organization')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to='users.AccountUser')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_course', to='users.Course', verbose_name='Course')),
                ('students', models.ManyToManyField(to='users.Student')),
            ],
        ),
    ]
