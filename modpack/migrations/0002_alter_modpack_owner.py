# Generated by Django 4.2 on 2023-06-12 12:50

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modpack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modpack',
            name='owner',
            field=models.ForeignKey(default=accounts.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
