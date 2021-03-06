# Generated by Django 2.1.1 on 2019-03-04 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('body', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Get_Posts', to='blog.Category')),
            ],
            options={
                'verbose_name': '文章列表',
                'verbose_name_plural': '文章列表',
            },
        ),
    ]
