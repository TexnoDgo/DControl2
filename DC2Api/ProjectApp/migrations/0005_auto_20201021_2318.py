# Generated by Django 3.1.2 on 2020-10-21 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='active_project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ProjectApp.project'),
        ),
    ]
