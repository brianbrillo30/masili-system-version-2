# Generated by Django 4.1.1 on 2022-10-01 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnnouncementManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='body',
            field=models.TextField(max_length=500),
        ),
    ]
