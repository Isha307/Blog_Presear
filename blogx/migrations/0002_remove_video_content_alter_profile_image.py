# Generated by Django 4.0.4 on 2022-05-28 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogx', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='content',
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=False, upload_to='profile_pic'),
        ),
    ]
