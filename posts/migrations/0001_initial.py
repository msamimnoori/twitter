# Generated by Django 3.2.6 on 2021-10-01 18:01

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank='False', db_index=True, default='Anonymous', max_length=14, verbose_name='Name')),
                ('body', models.CharField(blank=True, db_index=True, max_length=140, null=True, verbose_name='Body')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('like_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='like_count')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created DateTime')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
