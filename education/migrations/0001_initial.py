# Generated by Django 3.0.8 on 2021-02-26 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sacco', '0002_nationalstaffmember_saccomember_saccostaffmember'),
        ('users', '0009_auto_20210226_0835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('course_name', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('course_length', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EducationDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('mission', models.TextField(blank=True, null=True)),
                ('vision', models.TextField(blank=True, null=True)),
                ('statement', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
                ('video', models.FileField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
                ('sacco', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sacco.SACCO')),
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
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='education.Course', verbose_name='Course')),
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
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutor_id', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('signup_date', models.DateTimeField(auto_now=True)),
                ('education_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.EducationDepartment')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to='sacco.SaccoStaffMember', verbose_name='Tutor Account')),
                ('sacco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sacco.SACCO')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
                ('survey', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey', to='education.Survey', verbose_name='Survey')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('registration_date', models.DateTimeField(auto_now=True)),
                ('education_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.EducationDepartment')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to='users.AccountUser')),
                ('sacco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sacco.SACCO')),
            ],
        ),
        migrations.CreateModel(
            name='ModuleItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, null=True, upload_to='')),
                ('notes', models.TextField(blank=True, null=True)),
                ('upload_date', models.DateTimeField(auto_now=True)),
                ('module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='module', to='education.Module', verbose_name='Course')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='module_tutor', to='education.Tutor', verbose_name='Tutor'),
        ),
        migrations.AddField(
            model_name='course',
            name='education_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.EducationDepartment'),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education_department', to='education.EducationDepartment', verbose_name='Education Department'),
        ),
        migrations.AddField(
            model_name='course',
            name='lead_tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lead_tutor', to='education.Tutor', verbose_name='Tutor'),
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_course', to='education.Course', verbose_name='Course')),
                ('instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_instructor', to='education.Tutor', verbose_name='Class Instructor')),
                ('students', models.ManyToManyField(to='education.Student')),
            ],
        ),
    ]
