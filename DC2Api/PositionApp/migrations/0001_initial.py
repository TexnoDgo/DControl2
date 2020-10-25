# Generated by Django 3.1.2 on 2020-10-25 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ElementApp', '0001_initial'),
        ('OrderApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('code', models.CharField(max_length=13)),
                ('qr_code', models.ImageField(default=None, upload_to='POSITION_QR_CODE')),
                ('sticker', models.FileField(default=None, upload_to='POSITION_STICKER')),
                ('draw_pdf', models.FileField(default=None, upload_to='POSITION_DRAW_PDF')),
                ('assembly', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ElementApp.assembly')),
                ('detail', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ElementApp.detail')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OrderApp.order')),
            ],
        ),
    ]
