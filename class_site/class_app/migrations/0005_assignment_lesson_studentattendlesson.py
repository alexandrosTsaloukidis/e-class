# Generated by Django 3.1.5 on 2021-01-21 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('class_app', '0004_auto_20210121_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lesson_code', models.CharField(max_length=5)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAttendLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_app.lesson')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_app.student')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_file', models.FileField(upload_to='uploads/% Y/% m/% d/')),
                ('upload_date_time', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='class_app.lesson')),
            ],
        ),
    ]
