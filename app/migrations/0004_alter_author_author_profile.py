# Generated by Django 4.0.6 on 2022-11-28 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_course_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_profile',
            field=models.ImageField(upload_to='author'),
        ),
    ]
