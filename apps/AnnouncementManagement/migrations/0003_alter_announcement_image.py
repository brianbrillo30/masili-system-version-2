# Generated by Django 4.1.1 on 2022-10-02 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnnouncementManagement', '0002_alter_announcement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
