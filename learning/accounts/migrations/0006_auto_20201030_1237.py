# Generated by Django 3.1.2 on 2020-10-30 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_auto_20201028_0216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='student',
        ),
        migrations.AddField(
            model_name='contact',
            name='stu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stu', to=settings.AUTH_USER_MODEL),
        ),
    ]
