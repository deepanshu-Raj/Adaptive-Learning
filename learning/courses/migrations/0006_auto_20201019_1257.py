# Generated by Django 3.1.2 on 2020-10-19 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='enroll',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enroll',
            name='done',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]