# Generated by Django 2.2.10 on 2020-03-08 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LyncUp', '0004_auto_20200308_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]