# Generated by Django 3.1.5 on 2021-01-21 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_app', '0003_auto_20210121_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
