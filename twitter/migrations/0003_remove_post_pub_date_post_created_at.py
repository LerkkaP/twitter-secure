# Generated by Django 4.2.1 on 2024-08-28 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
