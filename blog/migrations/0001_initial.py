# Generated by Django 3.2.9 on 2021-11-11 16:05

import autoslug.fields
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogPostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_time', models.DateTimeField(auto_now_add=True)),
                ('blog_image', models.ImageField(max_length=259, upload_to='blog/')),
                ('blog_desc', tinymce.models.HTMLField()),
                ('blog_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='blog_title', unique=True)),
            ],
        ),
    ]