# Generated by Django 5.0.3 on 2024-03-20 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resume/'),
        ),
    ]