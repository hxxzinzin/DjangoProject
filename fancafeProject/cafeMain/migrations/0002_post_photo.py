# Generated by Django 4.2.20 on 2025-04-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeMain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='blog_photo', verbose_name='이미지'),
        ),
    ]
