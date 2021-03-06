# Generated by Django 3.1.2 on 2020-10-25 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('OrderApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ProjectApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('root_status', models.CharField(choices=[('DESIGNER', 'DESIGNER'), ('PRODUCTION', 'PRODUCTION'), ('GUEST', 'GUEST')], default='GUEST', max_length=100)),
                ('active_order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='OrderApp.order')),
                ('active_project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ProjectApp.project')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
