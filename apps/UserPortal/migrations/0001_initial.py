# Generated by Django 4.1.1 on 2022-10-04 14:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ResidentManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_status', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='ResidencyCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(default='Certificate of Residency', max_length=70)),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('date_requested', models.DateField(auto_now_add=True)),
                ('date_released', models.DateField(null=True)),
                ('purpose', models.CharField(max_length=255)),
                ('res_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ResidentManagement.residentsinfo')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='UserPortal.documentstatus')),
            ],
        ),
        migrations.CreateModel(
            name='clearance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(default='Barangay Clearance', max_length=70)),
                ('age', models.CharField(max_length=70)),
                ('purpose', models.CharField(max_length=70)),
                ('date_requested', models.DateField(auto_now_add=True)),
                ('date_released', models.DateField(null=True)),
                ('community_tax_num', models.CharField(max_length=70, null=True)),
                ('community_tax_date_issued', models.DateField(null=True)),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('res_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ResidentManagement.residentsinfo')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='UserPortal.documentstatus')),
            ],
        ),
        migrations.CreateModel(
            name='CertificateOfIndigency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(default='Certificate of Indigency', max_length=70)),
                ('age', models.CharField(max_length=70)),
                ('purpose', models.CharField(max_length=70)),
                ('date_requested', models.DateField(auto_now_add=True)),
                ('date_released', models.DateField(null=True)),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('res_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ResidentManagement.residentsinfo')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='UserPortal.documentstatus')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessPermit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(default='Business Permit', max_length=70)),
                ('business_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('business_nature', models.CharField(max_length=255)),
                ('owner', models.CharField(max_length=255)),
                ('residece_certificate_no', models.CharField(max_length=255)),
                ('date_requested', models.DateField(auto_now_add=True)),
                ('date_released', models.DateField(null=True)),
                ('issued_at', models.CharField(max_length=255)),
                ('capital_investment', models.CharField(max_length=255)),
                ('gross_sales', models.CharField(max_length=255)),
                ('previous_or', models.CharField(max_length=255)),
                ('date_issued', models.DateField(null=True)),
                ('previous_or_issued_at', models.CharField(max_length=255)),
                ('amount_collect', models.CharField(max_length=255)),
                ('paid_or', models.CharField(max_length=255)),
                ('paid_or_date_issued', models.DateField(null=True)),
                ('paid_or_issued_at', models.CharField(max_length=255)),
                ('amount_colledted', models.CharField(max_length=255)),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('res_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ResidentManagement.residentsinfo')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='UserPortal.documentstatus')),
            ],
        ),
        migrations.CreateModel(
            name='BuildingPermit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(default='Building Permit', max_length=70)),
                ('proposed_construction', models.CharField(max_length=255)),
                ('total_area', models.CharField(max_length=255)),
                ('estimated_cost', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('owner', models.CharField(max_length=255)),
                ('contractor', models.CharField(max_length=255)),
                ('prepared_by', models.CharField(max_length=255)),
                ('paid_under_or', models.CharField(max_length=255)),
                ('date_requested', models.DateField(auto_now_add=True)),
                ('date_released', models.DateField(null=True)),
                ('amount_paid', models.CharField(max_length=255)),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('res_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ResidentManagement.residentsinfo')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='UserPortal.documentstatus')),
            ],
        ),
    ]
