# Generated by Django 4.1.1 on 2022-10-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserPortal', '0005_clearance_community_tax_date_issued_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clearance',
            name='document_type',
            field=models.CharField(default='Barangay Clearance', max_length=70),
        ),
    ]