# Generated by Django 4.0.4 on 2022-05-26 17:05

from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogx', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'likes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'managed': False},
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='new blog', max_length=256)),
                ('content', froala_editor.fields.FroalaField()),
                ('series', models.IntegerField()),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='blog')),
                ('video', models.FileField(upload_to='video')),
                ('is_draft', models.BooleanField(default=False)),
                ('trending', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogx.profile')),
                ('subtegory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogx.subcategory')),
                ('tags', models.ManyToManyField(blank=True, to='blogx.tag')),
            ],
        ),
        migrations.AddField(
            model_name='subcategory',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogx.category'),
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ManyToManyField(blank=True, to='blogx.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogx.profile')),
            ],
            options={
                'db_table': 'Bookmark',
            },
        ),
    ]
