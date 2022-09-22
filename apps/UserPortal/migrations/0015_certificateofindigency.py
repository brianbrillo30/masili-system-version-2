# Generated by Django 4.1.1 on 2022-09-22 21:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ResidentManagement', '0003_rename_years_recided_residentsinfo_years_resided'),
        ('UserPortal', '0014_clearance_transaction_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateOfIndigency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=70)),
                ('purpose', models.CharField(max_length=70)),
                ('date_requested', models.DateField(auto_now=True)),
                ('date_released', models.DateField(null=True)),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('res_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ResidentManagement.residentsinfo')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='UserPortal.documentstatus')),
            ],
        ),
    ]
