# Generated by Django 4.0.6 on 2022-11-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_what_you_learn_requirements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirements',
            name='points',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='what_you_learn',
            name='points',
            field=models.CharField(max_length=500),
        ),
    ]