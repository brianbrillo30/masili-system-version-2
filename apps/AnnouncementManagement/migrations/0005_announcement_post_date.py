# Generated by Django 4.1.1 on 2022-10-03 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnnouncementManagement', '0004_alter_announcement_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
