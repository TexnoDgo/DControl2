# Generated by Django 3.1.2 on 2020-10-25 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ProjectApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
                ('readiness', models.DateField(null=True)),
                ('table', models.FileField(default=None, upload_to='ORDERS_TABLE')),
                ('qr_code_list', models.FileField(default=None, upload_to='ORDERS_QR_CODE_LIST')),
                ('pdf_specification', models.FileField(default=None, upload_to='ORDER_PDF_SPECIFICATION')),
                ('draw_archive', models.FileField(default=None, upload_to='ORDERS_DRAW_ARCHIVE')),
                ('dxf_archive', models.FileField(default=None, upload_to='ORDERS_DXF_ARCHIVE')),
                ('part_archive', models.FileField(default=None, upload_to='ORDERS_PART_ARCHIVE')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectApp.project')),
            ],
        ),
    ]
