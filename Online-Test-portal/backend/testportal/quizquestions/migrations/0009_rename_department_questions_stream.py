# Generated by Django 5.0.3 on 2024-03-27 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizquestions', '0008_questions_branch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='department',
            new_name='stream',
        ),
    ]
