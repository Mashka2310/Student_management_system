# Generated by Django 5.0.1 on 2024-02-03 10:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=300)),
                ('course_fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_gender', models.CharField(max_length=300)),
                ('teacher_address', models.CharField(max_length=300)),
                ('teacher_phone', models.IntegerField()),
                ('teacher_age', models.IntegerField()),
                ('Image', models.ImageField(upload_to='image/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.coursemodel')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=300)),
                ('stuent_age', models.IntegerField()),
                ('student_address', models.CharField(max_length=300)),
                ('student_email', models.CharField(max_length=300)),
                ('Image', models.ImageField(upload_to='image/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.coursemodel')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.teachermodel')),
            ],
        ),
    ]
