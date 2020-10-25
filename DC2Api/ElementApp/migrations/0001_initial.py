# Generated by Django 3.1.2 on 2020-10-25 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assembly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
                ('draw_pdf', models.FileField(default=None, upload_to='ASSEMBLY_DRAW_PDF')),
                ('draw_pnf', models.ImageField(default=None, upload_to='ASSEMBLY_DRAW_PNG')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
                ('draw_pdf', models.FileField(default=None, upload_to='DETAIL_DRAW_PDF')),
                ('draw_pnf', models.ImageField(default=None, upload_to='DETAIL_DRAW_PNG')),
                ('dxf', models.FileField(default=None, upload_to='DETAIL_DXF')),
                ('part', models.FileField(default=None, upload_to='DETAIL_PART')),
                ('assembly', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ElementApp.assembly')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
